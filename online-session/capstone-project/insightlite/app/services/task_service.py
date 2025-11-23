from database import get_connection
from datetime import datetime
from models import Task 

def fetch_all_tasks():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]


def fetch_task(task_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


def create_task(data):
    conn = get_connection()
    cur = conn.cursor()
    created_at = datetime.utcnow().isoformat()
    cur.execute(
        "INSERT INTO tasks (title, description, priority, est_days, created_at, due_date) VALUES (?, ?, ?, ?, ?, ?)",
        (   
            data['title'],
            data.get('description',''),
            data.get('priority',1),
            data.get('est_days',1),
            created_at, data.get('due_date')
        )
    )
    conn.commit()
    task_id = cur.lastrowid
    conn.close()
    return task_id


def update_task(task_id: int, data):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
    "UPDATE tasks SET title=?, description=?, priority=?, est_days=?, due_date=?, completed=? WHERE id=?",
    (data['title'], data.get('description',''), data.get('priority',1), data.get('est_days',1), data.get('due_date'), data.get('completed',0), task_id)
    )
    conn.commit()
    conn.close()


def delete_task(task_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()


def stats_summary():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) as total FROM tasks")
    total = cur.fetchone()['total']
    cur.execute("SELECT COUNT(*) as completed FROM tasks WHERE completed=1")
    completed = cur.fetchone()['completed']
    conn.close()
    return {"total": total, "completed": completed, "pending": total - completed}


def fetch_pending_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE completed = 0")
    rows = cursor.fetchall()
    conn.close()

    return [Task(**dict(row)) for row in rows]