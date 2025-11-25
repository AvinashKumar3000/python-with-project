# project implementation

## folder structure

```bash
project_folder/
│
├── data/
│   └── expenses.csv
│
├── utils/
│   ├── __init__.py
│   └── exceptions.py
│   └── validators.py
│
├── services/
│   ├── __init__.py
│   └── expense_service.py
│   └── file_service.py
│
└── app.py
```

- all file and its code is given below

## `app.py`

```python
import services.expense_service as service 

def print_menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Total Expense")
    print("4. Exit")
    print("============================")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Category: ")
            amount = input("Amount: ")
            note = input("Note (optional): ")
            try:
                service.add_expense(category, amount, note)
                print("✔ Expense added successfully!")
            except Exception as e:
                print("Error:", e)

        elif choice == "2":
            records = service.get_all_expenses()
            if not records:
                print("No expenses found.")
            else:
                print("\n--- Expense Records ---")
                for row in records:
                    print(row)

        elif choice == "3":
            try:
                total = service.get_total_expense()
                print(f"Total Expense: ₹{total}")
            except Exception as e:
                print("Error:", e)

        elif choice == "4":
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
```

## `exceptions.py`

```python
class InvalidAmountError(Exception):
    """Raised when amount is invalid."""
    pass

class InvalidCategoryError(Exception):
    """Raised when category is invalid."""
    pass
```

## `validators.py`

```python
from utils.exceptions import InvalidAmountError, InvalidCategoryError

def validate_amount(amount):
    try:
        value = float(amount)
        if value < 0:
            raise InvalidAmountError("Amount must be positive.")
    except ValueError:
        raise InvalidAmountError("Amount must be a numeric value.")

def validate_category(category):
    if not category or not category.strip():
        raise InvalidCategoryError("Category cannot be empty.")
```

## `expense_service.py`

```python
import services.file_service as file_service
from utils.validators import validate_amount, validate_category

def add_expense(category, amount, note=""):
    validate_category(category)
    validate_amount(amount)
    row = [category.strip(), amount.strip(), note.strip()]
    file_service.write_row(row)

def get_all_expenses():
    return file_service.read_all()

def get_total_expense():
    records = file_service.read_all()
    total = 0
    for row in records:
        amount = row[1]
        try:
            total += float(amount)
        except ValueError:
            pass
    return total
```

## `file_service.py`

```python
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
```

## `expenses.csv`

```python
Category,Amount,Note
car,2000,nothing
food,400,breakfast and lunch
```
