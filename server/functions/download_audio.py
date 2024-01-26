import pytube
import random
import string

def download_audio(url):
    # Generate a random name for the audio file
    random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    audio_filename = f"{random_name}.mp3"

    # Create a YouTube object and get the video
    yt = pytube.YouTube(url)

    audio = yt.streams.get_audio_only()
    audio.download(filename=audio_filename)
    return audio_filename

