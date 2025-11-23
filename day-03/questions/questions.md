# **`DAY 03` QUESTIONS**

---

## **1. Which file mode is used only for reading a file?**

1. `"r"`
2. `"w"`
3. `"a"`
4. `"rw"`

answer: `1. "r"`

---

## **2. What happens when you open a file in `"w"` mode?**

1. File opens without changes
2. File opens and appends data
3. File is overwritten (content erased)
4. Error

answer: `3. File is overwritten`

---

## **3. What is the correct way to read a file?**

```python
f = open("data.txt", "r")
```

1. f.get()
2. f.read()
3. f.take()
4. f.load()

answer: `2. f.read()`

---

## **4. What does this code print?**

```python
f = open("test.txt", "a")
f.write("Hello")
f.close()
```

1. Deletes file
2. Overwrites file
3. Adds "Hello" at the end
4. Error

answer: `3. Adds "Hello" at the end`

---

## **5. What does `finally` block guarantee?**

1. Runs only if no error
2. Runs only if error occurs
3. Never runs
4. Always runs

answer: `4. Always runs`

---

## **6. Which built-in module helps with date and time?**

1. os
2. math
3. datetime
4. system

answer: `3. datetime`

---

## **7. Which function from `math` module returns square root?**

1. math.square()
2. math.sqrt()
3. math.root()
4. math.pow2()

answer: `2. math.sqrt()`

---

## **8. What does this code output?**

```python
import os
print(os.getcwd())
```

1. Name of OS
2. Current working directory
3. Home directory
4. Error

answer: `2. Current working directory`

---

## **9. What will happen?**

```python
try:
    x = 10 / 0
except:
    print("Error")
```

1. Crash
2. 0
3. "Error"
4. None

answer: `3. "Error"`

---

## **10. Which is mean by CSV ?**

1. Column Stored Values  
2. Comma Separated Values  
3. Common Shared Variables  
4. Character Separated Vector  

answer: `2. Comma Separated Values`

---

## **11. What is the output?**

```python
with open("data.txt", "w") as f:
    f.write("Hello")
print(f.closed)
```

1. False
2. True
3. Error
4. Depends

answer: `2. True`
*(file auto-closes)*

---

## **12. What does this CSV code do?**

```python
import csv
f = open("data.csv")
reader = csv.reader(f)
```

1. Writes CSV
2. Reads CSV rows
3. Deletes CSV
4. Converts CSV to JSON

answer: `2. Reads CSV rows`

---

## **13. Which is a valid user-defined module import?**

1. import myfile.py
2. import myfile
3. import myfile()
4. using myfile

answer: `2. import myfile`

---

## **14. What is printed?**

```python
try:
    print("A")
finally:
    print("B")
```

1. A
2. B
3. A B
4. Error

answer: `3. A B`

---

## **15. What does this code do?**

```python
import math
print(math.floor(5.9))
```

1. 6
2. 5
3. 4
4. Error

answer: `2. 5`

---

## **16. What will be stored in `content`?**

```python
f = open("text.txt", "r")
content = f.readline()
```

1. Entire file
2. One line
3. Last line
4. None

answer: `2. One line`

---

## **17. What does `"a"` mode do?**

1. Opens file and clears content
2. Opens for reading only
3. Appends to file
4. Opens in binary

answer: `3. Appends to file`

---

## **18. What is the output?**

```python
import datetime
x = datetime.date.today()
print(x.year > 2000)
```

1. True
2. False
3. Error
4. Current year

answer: `1. True`

---

## **19. What does this code do?**

```python
import os
os.remove("old.txt")
```

1. Renames file
2. Deletes file
3. Moves file
4. Opens file

answer: `2. Deletes file`

---

## **20. What will this code print?**

```python
import math
print(math.pow(2, 3))
```

1. 6.0
2. 8.0
3. 2.0
4. Error

answer: `2. 8.0`

---

## **21. What happens when reading student data?**

```python
with open("students.txt") as f:
    print(f.read())
```

1. Writes students
2. Reads all students
3. Deletes file
4. Error

answer: `2. Reads all students`

---

## **22. What does this code do?**

```python
try:
    x = int("abc")
except ValueError:
    print("Invalid")
```

1. Error
2. “abc”
3. "Invalid"
4. None

answer: `3. "Invalid"`

---

## **23. What is the output of writing a list to a file?**

```python
f = open("a.txt", "w")
f.write(str([1,2,3]))
f.close()
```

1. 1 2 3
2. [1,2,3]
3. Error
4. Nothing

answer: `2. [1,2,3]`

---

## **24. What does this user module code print?**

`utils.py`:

```python
def greet():
    return "Hello"
```

Main:

```python
import utils
print(utils.greet())
```

1. utils
2. greet
3. Hello
4. Error

answer: `3. Hello`

---

## **25. What does this represent (Mini Project Concept)?**

```python
amount = int(input())
category = input()
f = open("expense.csv", "a")
f.write(f"{amount},{category}\n")
f.close()
```

1. Clears all expenses
2. Reads expenses
3. Adds a new expense to file
4. Deletes expenses

answer: `3. Adds a new expense to file`
