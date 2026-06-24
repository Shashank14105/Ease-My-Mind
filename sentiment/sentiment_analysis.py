from transformers import pipeline
import streamlit as st

# Load sentiment model once
@st.cache_resource
def load_sentiment_model():
    return pipeline(
        "sentiment-analysis",
        model="cardiffnlp/twitter-roberta-base-sentiment"
    )

sentiment_pipeline = load_sentiment_model()

def analyze_sentiment(text):

    result = sentiment_pipeline(text)

    label = result[0]["label"]

    if label == "LABEL_2":
        return "Positive"

    elif label == "LABEL_1":
        return "Neutral"

    else:
        return "Negative"

