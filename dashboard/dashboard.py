import sqlite3
import pandas as pd


def load_data():

    conn = sqlite3.connect("database/mood_history.db")

    df = pd.read_sql_query(
        "SELECT * FROM mood_logs",
        conn
    )

    conn.close()

    return df