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



```python
from functools import reduce

# List of student names
students = ["Aarav", "Meera", "John", "Kavya", "Rohit", "Ananya", "Dev"]

# -----------------------------
# 1. SORTING using reduce
# (Note: reduce is not ideal for sorting, but we can simulate insertion sort)
# -----------------------------
def insert_sorted(sorted_list, name):
    """Insert 'name' into the sorted_list at correct position."""
    for i in range(len(sorted_list)):
        if name < sorted_list[i]:
            return sorted_list[:i] + [name] + sorted_list[i:]
    return sorted_list + [name]

sorted_students = reduce(insert_sorted, students, [])
print("Sorted Students:")
print(sorted_students)

# -----------------------------
# 2. FILTERING using filter()
# -----------------------------
# Filter names starting with 'A'
starts_with_A = list(filter(lambda name: name.startswith("A"), students))
print("\nStudents starting with A:")
print(starts_with_A)

# Filter names with length > 4
long_names = list(filter(lambda name: len(name) > 4, students))
print("\nNames longer than 4 characters:")
print(long_names)

# -----------------------------
# 3. Using map() example
# Convert names to uppercase
# -----------------------------
uppercase_names = list(map(lambda name: name.upper(), students))
print("\nNames in UPPERCASE:")
print(uppercase_names)
```
