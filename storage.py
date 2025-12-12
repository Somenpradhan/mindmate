import os
import json
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
HISTORY_FILE = os.path.join(DATA_DIR, "mood_history.json")

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def save_entry(entry: dict):
    history = load_history()
    history.append(entry)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

def create_entry(text, analysis):
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "text": text,
        "mood": analysis.get("mood"),
        "score": analysis.get("score"),
        "summary": analysis.get("summary"),
        "tips": analysis.get("tips"),
        "journaling_prompt": analysis.get("journaling_prompt"),
    }
