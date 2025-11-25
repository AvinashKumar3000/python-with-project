# solution

```python
import json

file_name = "students.json"

# Step 1: Read JSON from same file
with open(file_name, "r") as f:
    students = json.load(f)

print("Before update:")
print(students)

# 👉 You can modify the list here
# Example: Add one more student
students.append({"id": 13, "name": "example", "age": 20})

# Step 2: Write back to the *same* file
with open(file_name, "w") as f:
    json.dump(students, f, indent=4)

print("Updated and written back to same file.")


```
