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
