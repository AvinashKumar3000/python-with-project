import csv
import os

class FileService:

    FILE_PATH = "data/expenses.csv"

    def __init__(self):
        # Create file if not exists
        if not os.path.exists("data"):
            os.makedirs("data")

        if not os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Category", "Amount", "Note"])

    def write_row(self, row):
        with open(self.FILE_PATH, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(row)

    def read_all(self):
        with open(self.FILE_PATH, "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            return list(reader)
