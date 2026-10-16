from fastapi import APIRouter, HTTPException, status

import nltk

nltk.data.path.append("./nltk_data")

from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.parsers.plaintext import PlaintextParser

from models.summary import SummarizeRequest, SummarizeResponse
from functions.download_transcript import TranscriptUnavailableError, VideoTranscription

router = APIRouter()

video_transcriber = VideoTranscription()


@router.post("/summarize", response_model=SummarizeResponse)
async def summarize(payload: SummarizeRequest):
    try:
        video_id, transcript = video_transcriber.get_video_transcription(str(payload.url))

        if not transcript:
            raise ValueError("Transcript could not be fetched or is empty.")

        parser = PlaintextParser.from_string(transcript, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary_sentences = summarizer(parser.document, 5)  # Summarize to 5 sentences

        summary = " ".join(str(sentence) for sentence in summary_sentences)
        return SummarizeResponse(summary=summary, transcript=transcript, video_id=video_id, sentence_count=len(summary_sentences))
    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(error)) from error
    except TranscriptUnavailableError as error:
        raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY, detail=str(error)) from error
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(error)) from error
