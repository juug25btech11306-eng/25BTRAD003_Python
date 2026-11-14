import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

def load_data(filename):
    path = DATA_DIR / filename
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []

def save_data(filename, records):
    path = DATA_DIR / filename
    with path.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)
