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
