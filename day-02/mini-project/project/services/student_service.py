from utils.file_handler import load_data, save_data

def add_student(student_id, name, age):
    students = load_data()

    # Prevent duplicates
    for s in students:
        if s["id"] == student_id:
            return "Student ID already exists"

    students.append({"id": student_id, "name": name, "age": age})
    save_data(students)
    return "Student added successfully"

def get_all_students():
    return load_data()

def get_student(student_id):
    students = load_data()
    for s in students:
        if s["id"] == student_id:
            return s
    return None

def update_student(student_id, name=None, age=None):
    students = load_data()
    for s in students:
        if s["id"] == student_id:
            s["name"] = name
            s["age"] = age
            save_data(students)
            return "Student updated successfully"

    return "Student not found"

def delete_student(student_id):
    students = load_data()
    new_students = [s for s in students if s["id"] != student_id]

    if len(students) == len(new_students):
        return "Student not found"

    save_data(new_students)
    return "Student deleted successfully"
