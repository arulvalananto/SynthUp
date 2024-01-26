import requests
import json

def fetch_captions(caption_url):
    try:
        response = requests.get(caption_url)
        response.raise_for_status()

        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching captions: {e}")
        return None
    
def write_captions_to_file(captions, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(captions)
        print(f"Captions written to {file_path}")
    except Exception as e:
        print(f"Error writing captions to file: {e}")
        

def extract_text_segments(json_data):
    try:
        # Parse JSON
        data = json.loads(json_data)

        # Extract text segments from "segs" key
        text_segments = [seg["utf8"] for event in data.get("events", []) for seg in event.get("segs", [])]

        return text_segments
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None