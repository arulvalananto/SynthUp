"""
This module contains the download_audio function, which downloads 
audio from a given URL and saves it as an MP3 file.
"""

import random
import string

import pytube

def download_audio(url):
    """
    Downloads audio from a given URL and saves it as an MP3 file.

    Args:
        url (str): The URL of the audio to be downloaded.

    Returns:
        str: The filename of the downloaded audio file.
    """
    # Generate a random name for the audio file
    random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    audio_filename = f"{random_name}.mp3"

    # Create a YouTube object and get the video
    yt = pytube.YouTube(url)

    audio = yt.streams.get_audio_only()
    audio.download(filename=audio_filename)
    return audio_filename
