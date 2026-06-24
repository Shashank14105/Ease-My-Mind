import streamlit as st
import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "models", "stress_model.pkl")
encoder_path = os.path.join(BASE_DIR, "models", "label_encoders.pkl")

# Load Model and Encoders
@st.cache_resource
def load_resources():
    model = joblib.load(model_path)
    encoders = joblib.load(encoder_path)
    return model, encoders

model, encoders = load_resources()


def calculate_stress_score(
        academic_pressure,
        study_satisfaction,
        study_hours,
        financial_stress,
        social_interaction,
        exercise,
        screen_time):

    score = (
        academic_pressure*2 + financial_stress*2 + study_hours+ screen_time - study_satisfaction - social_interaction - exercise*2
    )

    if score <= 10:
        return "Low"
    elif score <= 20:
        return "Moderate"
    else:
        return "High"


def predict_stress(
        gender,
        age,
        academic_pressure,
        study_satisfaction,
        sleep_duration,
        dietary_habits,
        study_hours,
        financial_stress,
        social_interaction,
        exercise,
        screen_time):

    # Encode categorical variables
    gender = encoders["gender"].transform([gender])[0]
    sleep_duration = encoders["sleep"].transform([sleep_duration])[0]
    dietary_habits = encoders["diet"].transform([dietary_habits])[0]

    # Create dataframe
    data = pd.DataFrame([{
        "Gender": gender,
        "Age": age,
        "Academic Pressure": academic_pressure,
        "Study Satisfaction": study_satisfaction,
        "Sleep Duration": sleep_duration,
        "Dietary Habits": dietary_habits,
        "Study Hours": study_hours,
        "Financial Stress": financial_stress,
        "Social Interaction": social_interaction,
        "Exercise": exercise,
        "Screen Time": screen_time
    }])

    # Depression prediction
    depression_risk = model.predict(data)[0]

    # Lifestyle stress score
    stress_score = calculate_stress_score(
        academic_pressure,
        study_satisfaction,
        study_hours,
        financial_stress,
        social_interaction,
        exercise,
        screen_time
    )

    # Hybrid decision
    if depression_risk == "No":

        if stress_score == "Low":
            return "Low Stress"

        elif stress_score == "Moderate":
            return "Moderate Stress"

        else:
            return "Moderate Stress"

    else:

        if stress_score == "Low":
            return "Moderate Stress"

        else:
            return "Severe Stress"