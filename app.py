import streamlit as st
import pandas as pd
import plotly.express as px

from prediction.stress_predictor import predict_stress
from sentiment.sentiment_analysis import analyze_sentiment
from chatbot.gemini_chatbot import generate_advice, chat_with_memory
from database.save_log import save_log
from dashboard.dashboard import load_data
from alerts.alerts import check_risk, get_alert_message
from reports.generate_report import generate_pdf

st.set_page_config(
    page_title = "Ease My Mind",
    page_icon = "🧠"
)

#Session State Variables
if "prediction_done" not in st.session_state:
    st.session_state.prediction_done = False

if "final_result" not in st.session_state:
    st.session_state.final_result = None

if "emotion" not in st.session_state:
    st.session_state.emotion = None

if "advice" not in st.session_state:
    st.session_state.advice = None

if "report_ready" not in st.session_state:
    st.session_state.report_ready = False

if "warning_message" not in st.session_state:
    st.session_state.warning_message = None

if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None

page = st.sidebar.radio(
    "Navigation",
    [
        "Stress Prediction",
        "Analytics Dashboard",
        "🪷 Medhā AI"
    ]
)

#New Assessment Button
if st.sidebar.button("🔄 New Assessment"):

    st.session_state.prediction_done = False
    st.session_state.final_result = None
    st.session_state.emotion = None
    st.session_state.advice = None
    st.session_state.warning_message = None
    st.session_state.prediction_result = None
    st.session_state.report_ready = False

if page == "Stress Prediction":

    st.title("🧠 Ease My Mind")
    st.subheader("Ai Wellness & Stress Prediction System By Shashank")
    st.write("Fill these out to Calculate Your Stress")


    #User Input
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    age = st.slider(
        "Age",
        15,
        40,
        20
    )

    academic_pressure = st.slider(
        "Academic Pressure",
        1,
        10,
        5
    )

    study_satisfaction = st.slider(
        "Study Satisfaction",
        1,
        10,
        5
    )

    sleep_duration = st.selectbox(
        "Sleep Duration",
        [
            "Less than 5 hours",
            "5-6 hours",
            "7-8 hours",
            "More than 8 hours"
        ]
    )

    dietary_habits = st.selectbox(
        "Dietary Habits",
        [
            "Healthy",
            "Moderate",
            "Unhealthy"
        ]
    )

    study_hours = st.slider(
        "Study Hours",
        0,
        15,
        6
    )

    financial_stress = st.slider(
        "Financial Stress",
        1,
        10,
        5
    )

    social_interaction = st.slider(
        "Social Interaction",
        0,
        10,
        5
    )

    exercise = st.slider(
        "Exercise Hours",
        0,
        2,
        1
    )

    screen_time = st.slider(
        "Screen Time",
        0,
        12,
        6
    )

    journal = st.text_area(
        "📝 Daily Mood Journal",
        placeholder="How are you feeling today?"
    )

    #Predict Button 
    if st.button("Predict Stress"):
        st.session_state.prediction_done = True

        result = predict_stress(
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
            screen_time
        )

        # Sentiment Analysis
        if journal.strip() == "":
            emotion = "Neutral"
        else:
            emotion = analyze_sentiment(journal)

        # Combine Stress + Sentiment
        if result == "Low Stress":

            if emotion == "Negative":
                final_result = "Moderate Stress"

            else:
                final_result = "Low Stress"

        elif result == "Moderate Stress":

            if emotion == "Negative":
                final_result = "Severe Stress"

            elif emotion == "Positive":
                final_result = "Low Stress"

            else:
                final_result = "Moderate Stress"

        else:

            if emotion == "Positive":
                final_result = "Moderate Stress"

            else:
                final_result = "Severe Stress"

        #Display
        if final_result == "Low Stress":
            st.success("🟢 Low Stress")

        elif final_result == "Moderate Stress":
            st.warning("🟡 Moderate Stress")

        else:
            st.error("🔴 Severe Stress")

        st.session_state.final_result = final_result
        st.session_state.emotion = emotion

        with st.spinner("🤖 Generating personalized wellness recommendations..."):
            advice = generate_advice(
                final_result,
                emotion,
                sleep_duration,
                academic_pressure
            )

       
        st.session_state.advice = advice
        st.session_state.prediction_result = result
        save_log(
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
            screen_time,
            journal,
            emotion,
            final_result,
            advice
        )

        risk_df = check_risk()
        warning_message = get_alert_message(risk_df)
        st.session_state.warning_message = warning_message


    #New Changes Code Optimization
    if st.session_state.prediction_done:

        st.write(
            "Stress Prediction:",
            st.session_state.prediction_result
        )

        st.write(
            "😊 Journal Sentiment:",
            st.session_state.emotion
        )

        st.write(
            "Final Wellness Assessment:",
            st.session_state.final_result
        )
    
    if st.session_state.prediction_done:

        st.subheader("🤖 AI Wellness Coach")

        st.markdown(
            st.session_state.advice
        )

    if st.session_state.prediction_done:

        if st.session_state.final_result == "Low Stress":

            st.success("🟢 Low Stress")

        elif st.session_state.final_result == "Moderate Stress":

            st.warning("🟡 Moderate Stress")

        elif st.session_state.final_result == "Severe Stress":

            st.error("🔴 Severe Stress")

    
    #Alert Message (Prolonged Stress)
    if st.session_state.warning_message:

        st.warning(
            st.session_state.warning_message
        )

    #Download Report PDF Button
    if st.session_state.prediction_done:

        st.subheader("📄 Wellness Report")

        if st.button("Generate Wellness Report"):

            generate_pdf()

            st.session_state.report_ready = True

            st.success(
                "Report Generated Successfully!"
            )

        if st.session_state.report_ready:

            with open(
                "reports_output/wellness_report.pdf",
                "rb"
            ) as file:

                pdf_bytes = file.read()

            st.download_button(
                "⬇ Download Wellness Report",
                data=pdf_bytes,
                file_name="wellness_report.pdf",
                mime="application/pdf"
            )

elif page == "Analytics Dashboard":

    st.title("📊 Analytics Dashboard")

    df = load_data()
    
    stress_count = (
        df["stress_level"]
        .value_counts()
        .reset_index()
    )

    stress_count.columns = ["Stress Level", "Count"]

    fig = px.pie(
        stress_count,
        names="Stress Level",
        values="Count",
        title="Stress Distribution"
    )

    st.plotly_chart(fig)

    sentiment_count = (
        df["sentiment"]
        .value_counts()
        .reset_index()
    )

    sentiment_count.columns = ["Sentiment", "Count"]

    fig2 = px.bar(
        sentiment_count,
        x="Sentiment",
        y="Count",
        title="Sentiment Distribution"
    )

    st.plotly_chart(fig2)

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    #Create Timestamp
    daily = (
        df.groupby(df["timestamp"].dt.date)
        .size()
        .reset_index(name="count")
    )

    #Plot 
    fig3 = px.line(
        daily,
        x="timestamp",
        y="count",
        title="Daily Stress Entries",
        markers=True
    )

    st.plotly_chart(fig3)

    #Recent History
    st.subheader("Recent History")

    st.dataframe(
        df[
            [
                "timestamp",
                "stress_level",
                "sentiment"
            ]
        ].tail(10)
    )

elif page == "🪷 Medhā AI":
    st.title("🪷 Medhā AI")
    st.caption("Hello, I am Medhā, your wellness companion. How are you feeling today?")
    st.caption("Maa Saraswati will be kind to you 😌")

    question = st.text_area(
        "Ask anything",
        placeholder="I've been stressed for three days. What should I do?"
    )

    if st.button("Ask Medhā"):

        answer = chat_with_memory(question)

        st.write(answer)
