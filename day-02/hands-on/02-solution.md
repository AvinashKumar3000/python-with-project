# solution

```python
# Create a list of student names
students = ["Aarav", "Meera", "John", "Kavya", "Rohit", "Ananya", "Dev"]

# 1. Sorting the list
sorted_students = sorted(students)
print("Sorted Student Names:")
print(sorted_students)

# 2. Filtering names that start with 'A'
filtered_students = [name for name in students if name.startswith("A")]
print("\nStudents whose names start with A:")
print(filtered_students)

# 3. Filtering names with length > 4
long_names = [name for name in students if len(name) > 4]
print("\nStudents with names longer than 4 letters:")
print(long_names)

```
