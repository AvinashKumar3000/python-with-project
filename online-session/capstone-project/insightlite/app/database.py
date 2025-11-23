import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).parent.parent / "insightlite.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        priority INTEGER DEFAULT 1,
        est_days INTEGER DEFAULT 1,
        created_at TEXT,
        due_date TEXT,
        completed INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    init_db()
    print("DB initialized")