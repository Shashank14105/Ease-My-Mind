import sqlite3
import pandas as pd


def get_recent_history(limit=3):

    conn = sqlite3.connect("database/mood_history.db")

    query = f"""
    SELECT timestamp,
           stress_level,
           sentiment,
           journal
    FROM mood_logs
    ORDER BY timestamp DESC
    LIMIT {limit}
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df