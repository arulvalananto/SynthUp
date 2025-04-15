from fastapi import APIRouter

import nltk

nltk.data.path.append("./nltk_data")

from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.parsers.plaintext import PlaintextParser

from models.summary import SummarizeRequest
from functions.download_transcript import VideoTranscription

router = APIRouter()

video_transcriber = VideoTranscription()


@router.post("/summarize")
async def summarize(payload: SummarizeRequest):
    url = payload.url
    try:
        transcript = video_transcriber.get_video_transcription(url)

        if not transcript:
            raise ValueError("Transcript could not be fetched or is empty.")

        parser = PlaintextParser.from_string(transcript, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary_sentences = summarizer(parser.document, 5)  # Summarize to 5 sentences

        summary = " ".join(str(sentence) for sentence in summary_sentences)
        return {"summary": summary, "transcript": transcript, "error": None}
    except Exception as e:
        return {"summary": "", "transcript": "", "error": str(e)}
