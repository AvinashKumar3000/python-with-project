from services.student_service import (
    add_student,
    get_all_students,
    get_student,
    update_student,
    delete_student,
)

def menu():
    print("\n--------- Student Record Management ---------")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def main():
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            sid = int(input("Enter ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            result = add_student(sid, name, age)
            print(result)
        elif choice == "2":
            for s in get_all_students():
                print(s)
        elif choice == "3":
            sid = int(input("Enter ID: "))
            result = get_student(sid)
            print(result)
        elif choice == "4":
            sid = int(input("Enter ID: "))
            name = input("New Name (or press enter): ")
            age = input("New Age (or press enter): ")

            result = update_student(
                sid,
                name if name.strip() else None,
                int(age) if age.isdigit() else None,
            )
            print(result)
        elif choice == "5":
            sid = int(input("Enter ID: "))
            result = delete_student(sid)
            print(result)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
