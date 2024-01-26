import youtube_dlc
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi

from functions.common import fetch_captions, extract_text_segments


class VideoTranscription:
    def __init__(self) -> None:
        pass

    def __get_video_id(self, youtube_url):
        url_data = urlparse(youtube_url)
        query = parse_qs(url_data.query)
        video_id = query["v"][0]
        return video_id

    def __get_auto_captions(self, video_url):
        try:
            # Create a YoutubeDL object with options
            ydl_opts = {
                'writesubtitles': True,
                'allsubtitles': True,
                'writeautomaticsub': True,
                'skip_download': True,
            }
            with youtube_dlc.YoutubeDL(ydl_opts) as ydl:
                # Get video info
                info_dict = ydl.extract_info(video_url, download=False)

                # Check if automatic captions are available
                if 'automatic_captions' in info_dict:
                    auto_captions = info_dict['automatic_captions']

                    # Choose a language (e.g., 'en' for English)
                    language_code = 'en'

                    # Get auto-generated captions for the selected language
                    if language_code in auto_captions:
                        captions = auto_captions[language_code]
                        return captions

            print("Automatic captions not available for the specified language.")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

    def __get_caption(self, caption_urls):
        # Check if there are any caption URLs
        if caption_urls:
            # Get the first caption URL
            url = caption_urls[0]

            # Fetch the captions from the URL
            caption = fetch_captions(url['url'])

            # Check if any captions were fetched
            if caption:
                # Extract the text segments from the captions
                segments = extract_text_segments(caption)

                # Check if any segments were extracted
                if segments:
                    # Combine all the segments into a single string
                    subtitle = ''
                    for segment in segments:
                        subtitle += segment
                    return subtitle
                else:
                    # If no segments were extracted, print an error message and return None
                    print("Unable to fetch segments.")
                    return None
            else:
                # If no captions were fetched, print an error message and return None
                print("Unable_to fetch captions.")
                return None
        else:
            # If there are no caption URLs, print an error message and return None
            print("Unable to fetch auto-generated captions.")
            return None

    def get_video_transcription(self, youtube_url):
        """
        Retrieves the transcription of a YouTube video.

        Args:
            youtube_url (str): The URL of the YouTube video.

        Returns:
            str: The transcription of the video, or None if an error occurs.
        """
        try:
            # Parse the YouTube URL to extract the video ID
            video_id = self.__get_video_id(youtube_url)

            # Use the YouTubeTranscriptApi to get the transcript of the video
            transcript = YouTubeTranscriptApi.get_transcript(video_id)

            # If a transcript is found, join all the text parts together and return it
            if transcript:
                transcript = ' '.join([i['text'] for i in transcript])
                return transcript
            else:
                # If no transcript is found, try to get auto-generated captions
                caption_urls = self.__get_auto_captions(youtube_url)
                caption = self.__get_caption(caption_urls)
                return caption
        except Exception as e:
            # If an error occurs, print the error message and return None
            print(f"Error retrieving transcription: {str(e)}")
            return None
