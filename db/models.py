from db.database import get_connection


def get_sesion(chat_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sesiones WHERE chat_id = ?', (chat_id,))
    sesion = cursor.fetchone()
    conn.close()
    return sesion


def save_sesion(chat_id, historia_actual):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR REPLACE INTO sesiones (chat_id, historia_actual) 
    VALUES (?, ?)
    ''', (chat_id, historia_actual))
    conn.commit()
    conn.close()
