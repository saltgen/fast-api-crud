from datetime import datetime, timedelta
from typing import Optional, List

from pydantic import BaseModel, validator
from datetime import datetime
import pytz


def convert_iso_to_datetime(datetime_string):
    """
    Convert iso date in str format to datetime object
    """
    dt, _, us = datetime_string.partition(".")
    dt = datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S")
    us = int(us.rstrip("Z"), 10)
    return dt + timedelta(microseconds=us)


class AudioBase(BaseModel):
    id: Optional[int]

    title: str
    duration: int
    uploaded_time: str

    @validator('duration')
    def duration_validator(cls, duration):
        if duration <= 0:
            raise ValueError("Duration needs to be more than 0 seconds")
        return duration

    @validator('uploaded_time')
    def upload_time_validator(cls, uploaded_time):
        uploaded_time = convert_iso_to_datetime(uploaded_time).replace(tzinfo=pytz.utc)
        if uploaded_time < datetime.utcnow().replace(tzinfo=pytz.utc):
            raise ValueError("Upload time cannot be a timestamp from the past")
        return uploaded_time

    class Config:
        orm_mode = True


class SongCreate(AudioBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class PodcastCreate(AudioBase):

    host: str
    participants: Optional[List[str]] = None

    @validator('participants')
    def participants_validator(cls, participants):
        if participants:
            if len(participants) > 20:
                raise ValueError("Cannot allow more than 20 participants")

    class Config:
        orm_mode = True


class AudioBookCreate(AudioBase):

    id: Optional[int]
    author: str
    narrator: str

    class Config:
        orm_mode = True

