import sqlite3
import os

os.makedirs("database", exist_ok=True)
print(os.getcwd())

conn = sqlite3.connect("database/mood_history.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS mood_logs (

id INTEGER PRIMARY KEY AUTOINCREMENT,

timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

gender TEXT,
age INTEGER,

academic_pressure INTEGER,
study_satisfaction INTEGER,

sleep_duration TEXT,
dietary_habits TEXT,

study_hours INTEGER,
financial_stress INTEGER,

social_interaction INTEGER,
exercise INTEGER,
screen_time INTEGER,

journal TEXT,
sentiment TEXT,

stress_level TEXT,

gemini_advice TEXT

)
""")

conn.commit()

print("Database created successfully!")

conn.close()