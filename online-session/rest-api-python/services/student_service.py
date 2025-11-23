
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
