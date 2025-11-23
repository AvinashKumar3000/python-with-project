from services.file_service import FileService
from utils.validators import validate_amount, validate_category

class ExpenseService:

    def __init__(self):
        self.file_service = FileService()

    def add_expense(self, category, amount, note=""):
        validate_category(category)
        validate_amount(amount)

        row = [category.strip(), amount.strip(), note.strip()]
        self.file_service.write_row(row)

    def get_all_expenses(self):
        return self.file_service.read_all()

    def get_total_expense(self):
        records = self.file_service.read_all()
        total = 0
        for r in records:
            try:
                total += float(r[1])
            except ValueError:
                pass
        return total
