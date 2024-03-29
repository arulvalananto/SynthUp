"""
This module contains the summarize function.
"""

from summarizer import Summarizer


def summarize(transcript):
    """
    Summarizes the given transcript.

    Parameters:
        - transcript (str): transcription.

    Returns:
        - str: A summarized version of the transcript.

    Raises:
        - HTTPException: If there is an error in retrieving or processing the transcript.
    """
    model = Summarizer()
    return model(transcript, min_length=500, max_length=len(transcript) / 2)
