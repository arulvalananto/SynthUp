from pydantic import BaseModel, Field


class SummarizeRequest(BaseModel):
    url: str = Field(..., description="URL to summarize")
