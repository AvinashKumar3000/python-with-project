# project implementation

## folder structure

```bash
project_folder/
│
├── data/
│   └── students.json
│
├── utils/
│   ├── __init__.py
│   └── file_handler.py
│
├── services/
│   ├── __init__.py
│   └── student_service.py
│
└── app.py
```

- all file and its code is given below

## `app.py`

```python
from services.student_service import (
    add_student,
    get_all_students,
    get_student,
    update_student,
    delete_student,
)

def menu():
    print("\n--------- Student Record Management ---------")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def main():
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            sid = int(input("Enter ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            result = add_student(sid, name, age)
            print(result)
        elif choice == "2":
            for s in get_all_students():
                print(s)
        elif choice == "3":
            sid = int(input("Enter ID: "))
            result = get_student(sid)
            print(result)
        elif choice == "4":
            sid = int(input("Enter ID: "))
            name = input("New Name (or press enter): ")
            age = input("New Age (or press enter): ")

            result = update_student(
                sid,
                name if name.strip() else None,
                int(age) if age.isdigit() else None,
            )
            print(result)
        elif choice == "5":
            sid = int(input("Enter ID: "))
            result = delete_student(sid)
            print(result)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
```

## `file_handler.py`

```python
import json
import os

DATA_FILE = "data/students.json"

# Reads and returns student data from JSON file.
def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

# Saves student data into JSON file.
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
```

## `student_service.py`

```python
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
```

## `students.json`

```python
[
    {
        "id": 12,
        "name": "sample",
        "age": 23
    }
]
```
