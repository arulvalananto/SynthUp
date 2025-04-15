from fastapi import APIRouter
from models.summary import SummarizeRequest
from functions.download_transcript import VideoTranscription
from functions.summarize_transcript import TranscriptSummarizer

router = APIRouter()

video_transcriber = VideoTranscription()
transcript_summarizer = TranscriptSummarizer()


@router.post("/summarize")
async def summarize(payload: SummarizeRequest):
    url = payload.url

    try:
        transcript = video_transcriber.get_video_transcription(url)
        summary = transcript_summarizer.summarize(transcript)
        return {
            "summary": summary,
            "transcript": transcript,
        }
    except Exception as e:
        return {"error": str(e)}
