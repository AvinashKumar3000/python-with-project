import json
import os

DATA_FILE = "data/students.json"

def load_data():
    """Reads and returns student data from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_data(data):
    """Saves student data into JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
