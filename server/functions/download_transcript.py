from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from urllib.parse import urlparse, parse_qs
import re


class TranscriptUnavailableError(Exception):
    """Raised when YouTube cannot provide a usable caption track."""


class VideoTranscription:
    def __init__(self):
        self.client = YouTubeTranscriptApi()

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
        if parsed_url.netloc not in {"youtube.com", "www.youtube.com", "m.youtube.com"}:
            raise ValueError("Only public YouTube URLs are supported.")
        query_params = parse_qs(parsed_url.query)
        return query_params.get("v", [None])[0]

    def get_video_transcription(self, url: str) -> tuple[str, str]:
        """
        Downloads the transcript from YouTube.
        """
        video_id = self.extract_video_id(url)

        if not video_id:
            raise ValueError("Invalid YouTube URL.")

        try:
            # youtube-transcript-api 1.x exposes an instance-based fetch API.
            # Each returned snippet has a ``text`` attribute rather than being a dict.
            transcript = self.client.fetch(video_id)
            full_text = " ".join(snippet.text for snippet in transcript)
            return video_id, full_text

        except TranscriptsDisabled as error:
            raise TranscriptUnavailableError("Captions are disabled for this video.") from error
        except NoTranscriptFound as error:
            raise TranscriptUnavailableError("No captions are available for this video.") from error
        except Exception as error:
            raise TranscriptUnavailableError(
                "YouTube captions could not be reached right now. Please try again shortly or use another video."
            ) from error
