# setup file and folders

## database/students.json

```json
[
    {
        "id": 1,
        "name": "Aarav",
        "age": 20,
        "course": "Computer Science"
    },
    {
        "id": 2,
        "name": "Diya",
        "age": 21,
        "course": "Mechanical"
    }
]
```

## utils/file_ops.py

```python
import json
import os

DATA_FILE = os.path.join("database", "students.json")

def read_students():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def write_students(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

```

## utils/email_ops.py

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"
RECEIVER_EMAIL = "receiver_email@gmail.com"

def send_email(subject, body):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        print("📧 Email sent successfully!")
    except Exception as e:
        print("❌ Error sending email:", e)

```

## utils/scheduler.py

```python
import os
import time
import schedule
from datetime import datetime
from utils.email_ops import send_email

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def create_log():
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    log_file = os.path.join(LOG_DIR, f"log-{timestamp}.txt")

    # Prepare log content
    log_content = f"Log generated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\nSystem check: OK\nAPI running fine."

    # Send email before writing new log
    send_email(subject=f"Student API Log - {timestamp}", body=log_content)

    # Write log file
    with open(log_file, "w") as f:
        f.write(log_content)

    print(f"📝 Log created: {log_file}")

def start_scheduler():
    schedule.every(5).minutes.do(create_log)
    print("⏳ Scheduler started (runs every 5 minutes)...")

    while True:
        schedule.run_pending()
        time.sleep(1)

```

