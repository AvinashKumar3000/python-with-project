# variables and operators

## variables

A variable name (identifier) is the name you give to store some data in Python’s memory.

```python
age = 25
name = "Avinash"
```

### Rules for Variable Names in Python


### Rule 1: Only letters (A–Z, a–z), digits (0–9), and underscore (_) are allowed.

```python
# VALID 
student1 = "Avi"
score_2025 = 98
user_name = "John"
userName = "Mike"   # CamelCase also fine
# INVALID 
stu#name = "Ravi"   # ❌ special character #
user@id = 45        # ❌ @ not allowed
class%score = 99    # ❌ % not allowed
```

### Rule 2: Variable names cannot start with a digit.

```python
# VALID
name1 = "Avi"
_1student = "John"
# INVALID
1name = "Avi"     # ❌ starts with digit
2025_score = 100  # ❌ starts with digit
```

### RULE 3: Variable names are case-sensitive.

```python
name = "avi"
Name = "Avi"
NAME = "AVINASH"

print(name)  # avi
print(Name)  # Avi
print(NAME)  # AVINASH
```

### Rule 4: Variable names cannot be a Python keyword.

```python
class = "BCA"    # ❌ invalid
for = 10         # ❌ invalid
if = 5           # ❌ invalid
# You can still use them by adding an underscore:
class_ = "BCA"
for_ = 10
# check python keywords
import keyword
print(keyword.kwlist)
```

### Rule 5: Variable names can start with an underscore (_).

```python
_name = "Hidden"
__score = 99
_ = "temporary value"   # Even a single underscore is valid
```

### Rule 6: No spaces allowed.

You must use underscores or camelCase instead.

```python
# valid
user name = "Avi"    # ❌ space not allowed
total marks = 100    # ❌ invalid
# invalid
user_name = "Avi"     # ✅ snake_case
totalMarks = 100      # ✅ camelCase
```

### Rule 7: Variable names can be of any length (but short and meaningful is best).

```python
# Valid:
x = 5
total_number_of_students_in_class = 45
```

### Rule 8: Unicode characters are allowed (Python 3 feature).

You can use non-English characters or even emojis (rarely recommended).

```python
नाम = "अविनाश"
π = 3.14
😊 = "Happy"
```

### Rule 9: Don’t use built-in function names as variables (not an error, but bad practice).

```python
list = [1, 2, 3]   # Valid but ❌ bad practice (you lose access to list() function)
sum = 10           # Valid but ❌ hides built-in sum()

## INSTEAD KEEP THIS.
my_list = [1, 2, 3]
total_sum = 10
```



