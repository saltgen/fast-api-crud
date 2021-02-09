import datetime

from app.constants import ModelName
from app.models import Song, Podcast, AudioBook
from app.schemas import SongCreate, PodcastCreate, AudioBookCreate
from database import SessionLocal


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_model_type(audio_type):

    if audio_type == ModelName.song:
        return Song
    elif audio_type == ModelName.podcast:
        return Podcast
    elif audio_type == ModelName.audiobook:
        return AudioBook


def get_schema_for_model(audio_type):

    if audio_type == ModelName.song:
        return SongCreate
    elif audio_type == ModelName.podcast:
        return PodcastCreate
    elif audio_type == ModelName.audiobook:
        return AudioBookCreate
