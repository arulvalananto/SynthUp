from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from functions.download_transcript import VideoTranscription

app = FastAPI()
video_transcription = VideoTranscription()

class TranscriptRequest(BaseModel):
    youtube_url: str

@app.post("/download-transcript")
def download_transcript_handler(request: TranscriptRequest):
    youtube_url = request.youtube_url

    try:
        transcript = video_transcription.get_video_transcription(youtube_url)
        if transcript is None:
            raise HTTPException(status_code=400, detail="Could not retrieve transcript")

        return {"message": "Transcript downloaded successfully", "transcript": transcript}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))