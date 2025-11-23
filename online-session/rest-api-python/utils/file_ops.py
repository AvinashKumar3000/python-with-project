import json
import os

DATA_FILE = os.path.join("database", "students.json")

def read_students():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def write_students(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
