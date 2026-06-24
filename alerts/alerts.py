import sqlite3
import pandas as pd


def check_risk():

    conn = sqlite3.connect("database/mood_history.db")

    query = """
    SELECT timestamp,
           stress_level,
           sentiment
    FROM mood_logs
    ORDER BY timestamp DESC
    LIMIT 7
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df

#Detect Consecutive Severe Stress
def severe_stress_alert(df):

    max_consecutive = 0
    current = 0

    for stress in df["stress_level"]:

        if stress == "Severe Stress":
            current += 1
            max_consecutive = max (max_consecutive, current)
        
        else:
            current = 0
    
    return max_consecutive >=3

#Detect Persistent Negative Sentiment

def negative_sentiment_alert(df):

    max_consecutive = 0
    current = 0

    for sentiment in df["sentiment"]:

        if sentiment == "Negative":
            current += 1
            max_consecutive = max(max_consecutive, current)

        else:
            current = 0

    return max_consecutive >= 3

#Create Wellness Message 
def get_alert_message(df):

    stress_alert = severe_stress_alert(df)
    sentiment_alert = negative_sentiment_alert(df)

    if stress_alert and sentiment_alert:

        return """
⚠️ Elevated Risk Detected

You're experiencing recurring stress and negative emotions.

• Try reducing workload temporarily.
• Talk to trusted friends or family.
• Practice sleep hygiene and regular breaks.
• Consider seeking support from a counselor if these feelings persist.
"""

    elif stress_alert:

        return """
⚠️ High Stress Pattern Detected

You have experienced severe stress several times recently.

Please prioritize sleep, hydration, practice meditation and Yoga.
Try to remain Calm reach out to the person nearest to you.
"""

    elif sentiment_alert:

        return """
⚠️ Persistent Negative Mood Detected

Your journal entries show recurring negative emotions.

Try mindfulness, exercise, meditation or reaching out to someone you trust.
"""

    else:

        return None
    
