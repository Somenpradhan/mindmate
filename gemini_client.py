import os
import json
import re
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

def call_gemini_api(prompt: str):
    if not API_KEY:
        return None
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
        headers = {"Content-Type": "application/json"}
        data = {"contents": [{"parts": [{"text": prompt}]}]}
        r = requests.post(url, headers=headers, json=data, timeout=20)
        if r.status_code == 200:
            out = r.json()
            text = out["candidates"][0]["content"]["parts"][0]["text"]
            return text
        else:
            print("Gemini API error:", r.text)
            return None
    except Exception as e:
        print("Gemini API call failed:", e)
        return None

def _extract_json(text: str):
    if not text:
        return None
    start, end = text.find("{"), text.rfind("}")
    if start != -1 and end != -1:
        try:
            return json.loads(text[start:end+1])
        except Exception:
            pass
    try:
        return json.loads(text.strip())
    except Exception:
        return None

def heuristic_analysis(text: str):
    pos = ["happy", "good", "great", "joy", "excited", "relaxed", "love", "awesome", "content"]
    neg = ["sad", "depressed", "anxious", "stressed", "angry", "worried", "lonely", "tired"]
    score = 50
    text_low = text.lower()
    for p in pos:
        if p in text_low:
            score += 8
    for n in neg:
        if n in text_low:
            score -= 8
    score = max(0, min(100, score))
    mood = "positive" if score >= 65 else "negative" if score <= 35 else "neutral"

    return {
        "mood": mood,
        "score": score,
        "summary": f"Heuristic suggests a {mood} mood (score {score}).",
        "tips": [
            "Take a 2-minute breathing break.",
            "Write one positive thing that happened today.",
            "Step away from your screen for 5 minutes."
        ],
        "journaling_prompt": "What’s one small action you can take to improve your mood right now?"
    }

def analyze_text(text: str):
    if not text.strip():
        return {
            "mood": "neutral",
            "score": 50,
            "summary": "No text provided.",
            "tips": ["Try writing a short sentence about how you're feeling."],
            "journaling_prompt": "What's happening right now?"
        }

    prompt = (
        "You are an empathetic mental health assistant. "
        "Analyze the user's journal entry and return ONLY a JSON object with keys: "
        "mood, score (0–100), summary, tips (array of 3 short strings), journaling_prompt.\n\n"
        f"User entry:\n{text}\n"
    )

    raw = call_gemini_api(prompt)
    parsed = _extract_json(raw)
    if parsed:
        parsed.setdefault("mood", "neutral")
        parsed.setdefault("score", 50)
        return parsed

    return heuristic_analysis(text)
