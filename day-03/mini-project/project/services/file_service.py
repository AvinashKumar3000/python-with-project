import csv
import os

FILE_PATH = "data/expenses.csv"

# Create file if not exists
if not os.path.exists("data"):
    os.makedirs("data")

if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Category", "Amount", "Note"])

def write_row(row):
    with open(FILE_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)

def read_all():
    with open(FILE_PATH, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        return list(reader)
