import json

def load_json(json_file):
    """Load and return JSON data from a file."""
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)
