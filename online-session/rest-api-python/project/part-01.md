# project

Student Management REST API (FastAPI + JSON + Scheduler + Email Logging)

```bash
student_api/
│
├── env/                      ← virtual environment
│
├── main.py                   ← FastAPI main app
├── database/
│   └── students.json         ← data file for student records
│
├── utils/
│   ├── file_ops.py           ← helper functions for JSON read/write
│   ├── email_ops.py          ← email sender function (SMTP)
│   └── scheduler.py          ← scheduler for logging
│
├── logs/
│   └── (auto generated) log-YYYYMMDD-HHMMSS.txt
│
└── requirements.txt          ← dependencies
└── services/
    └── student_service.py
```

## Setup Virtual Environment

```bash
# create virtual environment
python -m venv env
# for linux, mac
python3 -m venv env

# activate virtual environment
# Windows:
env\Scripts\activate

# Linux / Mac:
source env/bin/activate

# install dependencies
pip install -r requirements.txt
```

## requirements.txt

```bash
annotated-doc==0.0.4
annotated-types==0.7.0
anyio==4.11.0
click==8.3.0
colorama==0.4.6
fastapi==0.121.1
h11==0.16.0
httptools==0.7.1
idna==3.11
pydantic==2.12.4
pydantic_core==2.41.5
python-dotenv==1.2.1
PyYAML==6.0.3
schedule==1.2.2
sniffio==1.3.1
starlette==0.49.3
typing-inspection==0.4.2
typing_extensions==4.15.0
uvicorn==0.38.0
watchfiles==1.1.1
websockets==15.0.1
```
