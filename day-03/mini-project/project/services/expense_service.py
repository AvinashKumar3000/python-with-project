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
