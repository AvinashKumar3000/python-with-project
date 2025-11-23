import pandas as pd


class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath


def load_data(self):
    try:
        df = pd.read_csv(self.filepath)
        print("Data loaded successfully.\n")
        return df
    except Exception as e:
        print("Error loading data:", e)
        return None