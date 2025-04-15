from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from urllib.parse import urlparse, parse_qs
import re


class VideoTranscription:
    def __init__(self):
        pass

    def extract_video_id(self, url: str) -> str:
        """
        Extracts the YouTube video ID from a given URL.
        """
        # Handle short links like youtu.be/VIDEO_ID
        short_match = re.match(r"(https?://)?(www\.)?youtu\.be/([^?&]+)", url)
        if short_match:
            return short_match.group(3)

        # Handle full links like youtube.com/watch?v=VIDEO_ID
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        return query_params.get("v", [None])[0]

    def get_video_transcription(self, url: str) -> str:
        """
        Downloads the transcript from YouTube.
        """
        video_id = self.extract_video_id(url)

        if not video_id:
            raise ValueError("Invalid YouTube URL.")

        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            full_text = " ".join([entry["text"] for entry in transcript_list])
            return full_text

        except TranscriptsDisabled:
            raise Exception("Transcripts are disabled for this video.")
        except NoTranscriptFound:
            raise Exception("No transcript found for this video.")
        except Exception as e:
            raise Exception(f"Failed to fetch transcript: {e}")
