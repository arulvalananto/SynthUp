"""
FastAPI Application

This module contains the FastAPI application and its main route handler.
"""
from fastapi import FastAPI, HTTPException
from functions.summarize import summarize
from functions.download_transcript import VideoTranscription
from models.transcript import TranscriptRequest



app = FastAPI()
video_transcription = VideoTranscription()


@app.post("/download-transcript")
def download_transcript_handler(request: TranscriptRequest):
    """
    Handles the download of transcripts for a given YouTube video URL.

    Parameters:
    - request (TranscriptRequest): An object containing the YouTube URL.

    Returns:
    dict: A dictionary containing the success message and the downloaded transcript.

    Raises:
    HTTPException: If there is an error in retrieving or processing the transcript.
    """
    youtube_url = request.youtube_url

    try:
        transcript = video_transcription.get_video_transcription(youtube_url)
        if transcript is None:
            raise HTTPException(
                status_code=400, detail="Could not retrieve transcript")
        
        summarized_transcript = summarize(transcript)

        return {"message": "Transcript downloaded successfully", "transcript": transcript, "summary": summarized_transcript}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
