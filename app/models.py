
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import DateTime, ARRAY

from database import Base


class Audio(Base):
    """
    Abstract base class for creating other models
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    duration = Column(Integer, nullable=False)
    uploaded_time = Column(DateTime, nullable=False)

    class Config:
        orm_mode = True


class Song(Audio):

    __tablename__ = "songs"

    class Config:
        orm_mode = True


class Podcast(Audio):

    __tablename__ = "podcasts"

    host = Column(String(100), nullable=False)
    participants = Column(ARRAY(String(100)))


class AudioBook(Audio):

    __tablename__ = "audiobooks"

    author = Column(String(100), nullable=False)
    narrator = Column(String(100), nullable=False)


