from summarizer import Summarizer  # Install with `bert-extractive-summarizer`


class TranscriptSummarizer:
    def __init__(self):
        self.model = Summarizer()

    def summarize(self, text: str, ratio: float = 0.2) -> str:
        summary = self.model(text, ratio=ratio)
        return summary.strip()
