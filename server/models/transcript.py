"""
Models Module

This module contains Pydantic models representing data structures used in the application.

Classes:
- TranscriptRequest (BaseModel): Represents a request for transcript download from a YouTube video.
"""
from pydantic import BaseModel


class TranscriptRequest(BaseModel):
    """
    Represents a request for transcript download from a YouTube video.

    Attributes:
    - youtube_url (str): The URL of the YouTube video for which the transcript is requested.
    """
    youtube_url: str
