import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

from memory.memory import get_recent_history

api_key = st.secrets.get(
    "GOOGLE_API_KEY",
    os.getenv("GOOGLE_API_KEY")
)

genai.configure(api_key=api_key)

@st.cache_resource
def load_model():
    return genai.GenerativeModel(
        "gemini-2.5-flash-lite"
    )

model = load_model()

def generate_advice(
        stress_level,
        sentiment,
        sleep_duration,
        academic_pressure):

    prompt = f"""
You are a compassionate AI mental wellness assistant.

Stress Level: {stress_level}
Journal Sentiment: {sentiment}
Sleep Duration: {sleep_duration}
Academic Pressure: {academic_pressure}

Provide:

1. Personalized coping techniques.
2. A short study schedule.
3. Sleep recommendations.
4. Motivational advice and a quote.
5. One positive affirmation.

Keep the response supportive and concise.
"""
    print("========== GEMINI REQUEST ==========")
    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception:

        return """
    ### 🌿 AI Wellness Coach

    I'm temporarily unavailable because the Gemini API quota has been exhausted.

    Meanwhile:

    • Drink water
    • Take a short walk
    • Sleep adequately
    • Reduce screen time
    • Practice deep breathing

    The AI coach will become available again after quota reset.
    """

#AI Companion

def chat_with_memory(user_question):

    history = get_recent_history()

    context = ""

    for _, row in history.iterrows():

        context += f"""
Date: {row['timestamp']}
Stress Level: {row['stress_level']}
Sentiment: {row['sentiment']}
Journal: {row['journal']}
"""

    prompt = f"""
You are Ease My Mind AI.

Recent history:

{context}

User question:

{user_question}

Give supportive and practical advice.
Keep answers concise.
"""
    print("========== GEMINI REQUEST ==========")
    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception:

        return """
    ### 🌿 Medhā AI
    Hi I'm temporarily unavailable because the Gemini API quota has been exhausted.

    Meanwhile:

    • Drink water
    • Take a short walk
    • Sleep adequately
    • Reduce screen time
    • Practice deep breathing

    The Medhā AI will become available again after quota reset.
    """
