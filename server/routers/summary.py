from fastapi import APIRouter

from models.summary import SummarizeRequest

router = APIRouter()


@router.post("/summarize")
async def summarize(payload: SummarizeRequest):
    url = payload.url
    print(url)
    return {"summary": "This is a summary of the content at the provided URL."}
