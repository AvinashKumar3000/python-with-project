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
