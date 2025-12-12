import streamlit as st
from gemini_client import analyze_text
import storage
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="MindMate", page_icon="🧠", layout="centered")

# === 🎨 STYLING ===
st.markdown("""
<style>
/* Background gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #1e1f29 0%, #2a2d3e 40%, #1a1b24 100%);
    color: #ffffff;
}

/* Transparent header */
[data-testid="stHeader"] {
    background: rgba(0, 0, 0, 0);
}

/* Card style for containers */
.block-container {
    background: rgba(255, 255, 255, 0.05);
    padding: 2rem 3rem;
    border-radius: 20px;
    box-shadow: 0 0 25px rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(8px);
}

/* Buttons */
div.stButton > button:first-child {
    background: linear-gradient(90deg, #00c6ff 0%, #0072ff 100%);
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 1.05rem;
    padding: 0.5rem 1.2rem;
    box-shadow: 0 0 10px rgba(0, 114, 255, 0.4);
    transition: 0.3s;
}
div.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0 0 20px rgba(0, 114, 255, 0.6);
}

/* Text area */
textarea {
    background: rgba(255, 255, 255, 0.1) !important;
    color: #f8f9fa !important;
    border-radius: 10px !important;
}

/* DataFrame styling */
[data-testid="stDataFrame"] {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 10px;
    padding: 0.8rem;
}

/* Progress bar color */
[data-testid="stProgress"] > div > div {
    background: linear-gradient(90deg, #0072ff, #00c6ff);
}

/* Info boxes */
div.stAlert {
    border-radius: 10px;
}

/* Titles */
h1, h2, h3 {
    color: #00c6ff;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-thumb {
    background: #0072ff;
    border-radius: 4px;
}
</style>
""", unsafe_allow_html=True)

# === HEADER ===
st.title("🧠 MindMate — Your AI Mood & Wellness Companion")

# Gemini Key Status
if os.getenv("GEMINI_API_KEY"):
    st.success("✅ Gemini API connected successfully", icon="🤖")
else:
    st.warning("⚠️ Running in offline fallback mode (heuristic analysis only)", icon="⚙️")

st.write(
    "MindMate helps you reflect on your emotions through journaling. "
    "It uses Google's **Gemini AI** to analyze your mood and suggest mindfulness actions."
)

# === INPUT SECTION ===
st.markdown("## 📝 Journal Entry")
with st.form("journal_form"):
    text = st.text_area("How are you feeling today?", height=200, placeholder="Type freely about your thoughts, emotions, or day...")
    submitted = st.form_submit_button("💫 Analyze Mood")

if submitted:
    if not text.strip():
        st.error("Please write something first.")
    else:
        with st.spinner("Analyzing your entry with Gemini AI..."):
            result = analyze_text(text)

        mood = result["mood"].capitalize()
        score = result["score"]
        
        # Select emoji based on mood and score for better visual feedback
        mood_lower = result["mood"].lower()
        if mood_lower == "positive":
            if score >= 80:
                emoji = "😄"  # Very happy
            elif score >= 65:
                emoji = "😊"  # Happy
            else:
                emoji = "🙂"  # Slightly positive
        elif mood_lower == "negative":
            if score <= 20:
                emoji = "😢"  # Very sad
            elif score <= 35:
                emoji = "😔"  # Sad
            else:
                emoji = "😟"  # Worried
        elif mood_lower == "neutral":
            emoji = "😐"  # Neutral
        else:
            # Fallback based on score if mood is unexpected
            if score >= 80:
                emoji = "😄"
            elif score >= 65:
                emoji = "😊"
            elif score >= 50:
                emoji = "😐"
            elif score >= 35:
                emoji = "😟"
            else:
                emoji = "😔"

        st.markdown(f"### {emoji} **Mood:** {mood} — Score: {score}/100")
        st.progress(score)
        st.write(f"**Summary:** {result['summary']}")

        st.markdown("### 🪷 Coping Tips 🫂")
        for tip in result["tips"]:
            st.markdown(f"- {tip}")

        st.markdown(f"**Reflection Prompt:** {result['journaling_prompt']}")

        # Automatically save to mood history
        entry = storage.create_entry(text, result)
        storage.save_entry(entry)
        st.success("✅ Automatically saved to your mood history!")

# === HISTORY SECTION ===
st.markdown("---")
st.markdown("## 📊 Mood History")

history = storage.load_history()
if history:
    df = pd.DataFrame(history)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")
    st.line_chart(df.set_index("timestamp")["score"], height=300)
    st.dataframe(df[["timestamp", "mood", "score", "summary"]].tail(10))
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download History CSV", csv, "mood_history.csv", "text/csv")
else:
    st.info("No history yet — write your first reflection and save it to see your mood trends!")

# === FOOTER ===
st.markdown("""
---
<p style='text-align: center; color: #aaa;'>
Built with ❤️ using <b>Google Gemini API</b> & <b>Streamlit</b> for TFUG Build-a-thon 2025.
</p>
""", unsafe_allow_html=True)
