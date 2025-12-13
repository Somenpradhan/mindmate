# 🧠 MindMate — AI Mental Health & Wellness Companion

> *Your personal AI-powered mood analyst and wellness guide*

![MindMate](https://img.shields.io/badge/AI-Powered-blue?style=for-the-badge&logo=google&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)


## ✨ Features

- 📝 *Smart Journal Analysis* - Write freely about your thoughts and emotions
- 🎭 *AI Mood Detection* - Powered by Google Gemini AI for accurate sentiment analysis
- 📈 *Mood Scoring* - Get quantified mood scores (0-100) with visual progress bars
- 💡 *Personalized Coping Tips* - Receive tailored wellness suggestions
- 🤔 *Reflection Prompts* - Guided journaling questions for deeper self-awareness
- 📊 *Mood History Tracking* - Visualize your emotional journey over time
- 📱 *Beautiful UI* - Modern dark theme with smooth animations
- 🔄 *Offline Fallback* - Works without API key using heuristic analysis
- 📥 *Data Export* - Download your mood history as CSV

## 🎯 How It Works

1. *Write* - Share your thoughts in the journal entry box
2. *Analyze* - AI processes your text for emotional insights
3. *Discover* - Get mood analysis, coping strategies, and reflection prompts
4. *Track* - Your entries are automatically saved to build your mood timeline
5. *Reflect* - View historical trends and download your data

## 🚀 Quick Setup (5 minutes)

### Prerequisites
- Python 3.8+ installed
- Git (optional, for cloning)

### Installation

1. *Clone the repository*
   bash
   git clone https://github.com/amr7503/mindmate.git
   cd mindmate
   

2. *Create virtual environment*
   bash
   # On Windows
   python -m venv .venv
   .venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   

3. *Install dependencies*
   bash
   pip install -r requirements.txt
   

4. *Set up Gemini API (Recommended)*
   
   Create a .env file in the project root:
   env
   GEMINI_API_KEY=your_api_key_here
   
   
   Get your free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

5. *Run the application*
   bash
   streamlit run app.py
   

6. *Open in browser*
   
   Navigate to http://localhost:8501

## 🔧 Configuration

### Environment Variables

Create a .env file with the following:

env
GEMINI_API_KEY=your_gemini_api_key_here


### Without API Key

MindMate works offline with a built-in heuristic analyzer if no API key is provided. You'll see a warning but the app remains fully functional.

## 📁 Project Structure


mindmate/
├── app.py              # Main Streamlit application
├── gemini_client.py    # Google Gemini API integration
├── storage.py          # Data persistence and history management
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variables template
├── README.md          # This file
└── data/              # Auto-created directory for mood history
    └── mood_history.json


## 🛠 Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web application framework
- **[Google Gemini API](https://ai.google.dev/)** - Advanced AI text analysis
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation and analysis
- **[Python-dotenv](https://python-dotenv.readthedocs.io/)** - Environment configuration
- **[Requests](https://requests.readthedocs.io/)** - HTTP library for API calls

## 🎨 Features in Detail

### AI-Powered Analysis
- Uses Google's latest Gemini 2.5 Flash model
- Contextual understanding of emotions and sentiment
- Intelligent tip generation based on your specific situation

### Mood Visualization
- Dynamic emoji system reflecting mood intensity
- Interactive mood score charts
- Historical trend analysis with beautiful line graphs

### Data Privacy
- All data stored locally in JSON format
- No cloud storage or external data sharing
- Full control over your personal information

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

## 🙏 Acknowledgments

- Powered by *Google Gemini AI*
- UI framework by *Streamlit*
- Created with ❤ for mental health awareness
