import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "mood_history.db")


def save_log(
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
    sentiment,
    stress_level,
    gemini_advice
):

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO mood_logs(
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
        sentiment,
        stress_level,
        gemini_advice
        )

        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,

        (
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
            sentiment,
            stress_level,
            gemini_advice
        )
    )

    conn.commit()
    conn.close()