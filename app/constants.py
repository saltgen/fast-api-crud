from enum import Enum


class ModelName(str, Enum):
    song = "songs"
    podcast = "podcasts"
    audiobook = "audiobooks"
