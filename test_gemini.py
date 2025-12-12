import os
import requests
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GEMINI_API_KEY")
if not key:
    print("❌ No GEMINI_API_KEY found in .env")
    exit()

url = furl = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={key}"

payload = {
    "contents": [{"parts": [{"text": "Say hello Gemini"}]}]
}

r = requests.post(url, json=payload)
print("Status:", r.status_code)
print("Response:", r.text)
