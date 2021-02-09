
from typing import Optional

from fastapi import FastAPI, Depends, Query, HTTPException, Path
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.constants import ModelName
from app.utils import get_db, get_schema_for_model, get_model_type

app = FastAPI()


@app.post("/{audio_type}")
async def create_item(audio_type: ModelName, request: Request, db: Session = Depends(get_db)):
    _model_type = get_model_type(audio_type)
    _schema_type = get_schema_for_model(audio_type)
    data = await request.json()
    schema_object = _schema_type(**data)  # loading data into schema object, for validations
    entry_object = _model_type(**data)
    db.add(entry_object)
    db.commit()
    db.refresh(entry_object)
    return JSONResponse(content=jsonable_encoder(entry_object))


@app.get("/{audio_type}")
@app.get("/{audio_type}/{item_id}")
def get_item(audio_type: ModelName, item_id: Optional[int] = Query(None),  db: Session = Depends(get_db)):

    _model_type = get_model_type(audio_type)

    if not item_id:
        all_objects_queryset = db.query(_model_type).all()

        if all_objects_queryset:
            all_objects = [jsonable_encoder(item) for item in all_objects_queryset]
            return JSONResponse(content=all_objects)
        else:
            return f"No records found for item: {audio_type}"

    elif item_id > 0:
        _item = db.query(_model_type).filter(_model_type.id == item_id).first()
        if _item:
            return JSONResponse(content=jsonable_encoder(_item))
        else:
            raise HTTPException(status_code=400, detail="Item not found")
    else:
        raise HTTPException(status_code=400, detail="Invalid item id provided")


@app.patch("/{audio_type}/{item_id}")
async def update_item(audio_type: ModelName, request: Request, item_id: int, db: Session = Depends(get_db)):
    _model_type = get_model_type(audio_type)
    _schema_type = get_schema_for_model(audio_type)
    _item = db.query(_model_type).filter(_model_type.id == item_id).first()
    if _item:
        db.query(_model_type).filter(_model_type.id == item_id).delete()
        entry_dict = await request.json()
        entry_dict["id"] = item_id  # Persisting the original entry's id
        schema_object = _schema_type(**entry_dict)  # loading data into schema object, for validations
        entry_object = _model_type(**entry_dict)
        db.add(entry_object)
        db.commit()
        db.refresh(entry_object)
        return JSONResponse(content=jsonable_encoder(entry_object))
    else:
        raise HTTPException(status_code=400, detail="Item not found")


@app.delete("/{audio_type}/{item_id}")
def delete_item(audio_type: ModelName, item_id: int, db: Session = Depends(get_db)):

    _model_type = get_model_type(audio_type)

    if db.query(_model_type).filter(_model_type.id == item_id).first():
        db.query(_model_type).filter(_model_type.id == item_id).delete()
        db.commit()
        return f"Item {item_id} deleted successfully!"
    else:
        raise HTTPException(status_code=400, detail="Item not found")



