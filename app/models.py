
from datetime import datetime

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

    def save(self):
        if self.duration < 0:
            raise ValueError("Duration needs to be more than 0 seconds")

        if self.uploaded_time < datetime.now():
            raise ValueError("Upload time cannot be a timestamp from the past")


class Song(Audio):

    __tablename__ = "songs"


class Podcast(Audio):

    __tablename__ = "podcasts"

    host = Column(String(100), nullable=False)
    participants = Column(ARRAY(String))

    def save(self):
        """Data validation for participants field"""
        for _participant in self.participants:
            if len(_participant) > 100:
                raise ValueError("Participant's name cannot be more than 100 characters")
        
        if len(self.participants) > 20:
            raise ValueError("Cannot allow more than 20 participants")


class AudioBook(Audio):

    __tablename__ = "audiobooks"

    author = Column(String(100), nullable=False)
    narrator = Column(String(100), nullable=False)

