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
