from fastapi import FastAPI
from pydantic import BaseModel
import threading
from utils.scheduler import start_scheduler
from services.student_service import (
    get_all_students_service,
    get_student_by_id_service,
    add_student_service,
    update_student_service,
    delete_student_service
)

app = FastAPI(title="Student Management API")

# ✅ Data Model
class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str

# 🟢 Routes

@app.get("/students/")
def get_all_students():
    return get_all_students_service()

@app.get("/students/{student_id}")
def get_student(student_id: int):
    return get_student_by_id_service(student_id)

@app.post("/students/")
def add_student(student: Student):
    return add_student_service(student)

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    return update_student_service(student_id, updated_student)

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    return delete_student_service(student_id)

# 🔄 Scheduler Background Thread
@app.on_event("startup")
def start_background_scheduler():
    thread = threading.Thread(target=start_scheduler, daemon=True)
    thread.start()