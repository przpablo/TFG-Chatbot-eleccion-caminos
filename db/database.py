import sqlite3
from config.config import DB_PATH


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''DROP TABLE IF EXISTS sesiones;''')  # Borrar??
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sesiones (
        chat_id INTEGER PRIMARY KEY,
        historia_actual INTEGER
    )
    ''')
    conn.commit()
    conn.close()
