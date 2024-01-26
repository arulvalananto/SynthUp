"""
Common functions used by other functions
"""

import json
import requests

def fetch_captions(caption_url):
    """
    Fetches captions from the given URL.

    Args:
        caption_url (str): The URL to fetch the captions from.

    Returns:
        str: The fetched captions as text, or None if there was an error.

    Raises:
        requests.exceptions.RequestException: If there was an error fetching the captions.
    """
    try:
        response = requests.get(caption_url, timeout=200)
        response.raise_for_status()

        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching captions: {e}")
        return None

def write_captions_to_file(captions, file_path):
    """
    Write captions to a file.

    Args:
        captions (str): The captions to be written to the file.
        file_path (str): The path of the file to write the captions to.

    Returns:
        None

    Raises:
        Exception: If there is an error writing the captions to the file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(captions)
        print(f"Captions written to {file_path}")
    except IOError as e:
        print(f"Error writing captions to file: {e}")

def extract_text_segments(json_data):
    """
    Extracts text segments from JSON data.

    Args:
        json_data (str): JSON data containing text segments.

    Returns:
        list: List of text segments extracted from the JSON data.
            Returns None if there is an error decoding the JSON.
    """
    try:
        # Parse JSON
        data = json.loads(json_data)

        # Extract text segments from "segs" key
        text_segments = [seg["utf8"]
                         for event in data.get("events", []) for seg in event.get("segs", [])]

        return text_segments
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None
