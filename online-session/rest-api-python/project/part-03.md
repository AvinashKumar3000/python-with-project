# main code

## services/student_service.py

```python
from fastapi import HTTPException
from utils.file_ops import read_students, write_students

def get_all_students_service():
    """Return all students"""
    return read_students()

def get_student_by_id_service(student_id: int):
    """Return student by ID"""
    students = read_students()
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

def add_student_service(student):
    """Add a new student"""
    students = read_students()
    students.append(student.dict())
    write_students(students)
    return {"message": "Student added successfully", "student": student}

def update_student_service(student_id: int, updated_student):
    """Update a student record"""
    students = read_students()
    for i, s in enumerate(students):
        if s["id"] == student_id:
            students[i] = updated_student.dict()
            write_students(students)
            return {"message": "Student updated successfully"}
    raise HTTPException(status_code=404, detail="Student not found")

def delete_student_service(student_id: int):
    """Delete a student by ID"""
    students = read_students()
    new_students = [s for s in students if s["id"] != student_id]
    if len(new_students) == len(students):
        raise HTTPException(status_code=404, detail="Student not found")
    write_students(new_students)
    return {"message": "Student deleted successfully"}

```


## main.py

```python
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

```

## run the project

`uvicorn main:app --reload`
