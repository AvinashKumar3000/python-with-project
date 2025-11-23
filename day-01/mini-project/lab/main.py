def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "Fail"

def main():
    print("=== Student Marks & Grade Calculator ===")
    
    num_subjects = int(input("Enter number of subjects: "))
    marks = []
    
    for i in range(num_subjects):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)
    
    total = sum(marks)
    average = total / num_subjects
    grade = calculate_grade(average)
    
    print("\n----- Result -----")
    print(f"Total Marks: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    print("------------------")

if __name__ == "__main__":
    main()