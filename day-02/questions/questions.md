# `DAY 02` questions

---

**1. What will be the output of the following code?**

```python
names = ["ram", "abi", "john"]
print(sorted(names, reverse=True)[0])
```

1. ram
2. john
3. abi
4. ['ram','abi','john']

answer: `1. ram`

---

**2. Which list method removes and returns the *last* element by default?**

1. remove()
2. pop()
3. delete()
4. drop()

answer: `2. pop()`

---

**3. What happens if you try to modify a tuple element?**

```python
t = (1, 2, 3)
t[1] = 10
```

1. Nothing happens
2. It changes the value
3. Raises TypeError
4. Returns -1

answer: `3. Raises TypeError`

---

**4. What is the output?**

```python
a = {1,2,3}
b = {3,4,5}
print(a & b)
```

1. {1,2,3,4,5}
2. {3}
3. {1,2}
4. Error

answer: `2. {3}`

---

**5. What does this code print?**

```python
students = ["Avi", "Bala", "Charu", "Aisha"]
result = [s for s in students if s.startswith("A")]
print(result)
```

1. ["Avi"]
2. ["Avi", "Aish"]
3. ["Aish"]
4. []

answer: `2. ["Avi", "Aisha"]`

---

**6. What is the result of this set operation?**

```python
x = {1,2,3}
y = {3,4}
print(x - y)
```

1. {3}
2. {1,2}
3. {1,2,3,4}
4. {}

answer: `2. {1,2}`

---

**7. What will be the output?**

```python
record = {"name": "Avi", "marks": {"math": 90, "cs": 80}}
print(record["marks"]["cs"])
```

1. {"math": 90, "cs": 80}
2. cs
3. 80
4. Error

answer: `3. 80`

---

**8. Which of the following creates a dictionary using comprehension correctly?**

1. `{x: x*2 for x in range(3)}`
2. `{x, x*2 for x in range(3)}`
3. `(x: x*2 for x in range(3))`
4. `{x => x*2}`

answer: `1. {x: x*2 for x in range(3)}`

---

**9. What is the output?**

```python
names = ["ram", "ravi", "abi", "john"]
f = list(filter(lambda x: "a" in x, names))
print(f)
```

1. ["ram"]
2. ["ram", "ravi", "abi"]
3. ["abi", "john"]
4. Error

answer: `2. ["ram", "ravi", "abi"]`

---

**10. What does this program do?**

```python
students = {}
students["101"] = {"name": "Avi", "dept": "CSE"}
students["102"] = {"name": "Bala", "dept": "ECE"}
```

1. Creates two lists
2. Creates nested dictionaries
3. Updates a tuple
4. Creates a set inside dictionary

answer: `2. Creates nested dictionaries`

---

**11. What will be printed?**

```python
data = {"a": 1, "b": 2, "c": 3}
print(data.get("d", "Not Found"))
```

1. Error
2. None
3. d
4. Not Found

answer: `4. Not Found`

---

**12. What is the output?**

```python
t = (1, 2, [3,4])
t[2].append(5)
print(t)
```

1. Error because tuple is immutable
2. (1, 2, [3])
3. (1, 2, [3, 4, 5])
4. ([1,2], 3,4,5)

answer: `3. (1, 2, [3, 4, 5])`

---

**13. What does this list comprehension produce?**

```python
nums = [1,2,3]
print([n*n for n in nums])
```

1. [1,4,9]
2. [2,4,6]
3. [1,2,3]
4. (1,4,9)

answer: `1. [1,4,9]`

---

**14. What does this set operation do?**

```python
a = {1,2}
b = {2,3}
print(a ^ b)
```

1. {1,2,3}
2. {2}
3. {1,3}
4. {}

answer: `3. {1,3}`
*(Symmetric difference)*

---

**15. What will be the output?**

```python
students = [
    {"name": "Avi", "marks": 90},
    {"name": "Bala", "marks": 70},
    {"name": "Charu", "marks": 85}
]
topper = max(students, key=lambda x: x["marks"])
print(topper["name"])
```

1. Bala
2. Charu
3. Avi
4. Error

answer: `3. Avi`

---

**16. What will be the output of the following code?**

```python
lst = [1, 2, 3, 4]
print(lst[-2])
```

1. 2
2. 3
3. 4
4. Error

answer: `2. 3`

---

**17. What does this code do?**

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

1. [1, 2, 3]
2. [1, 2, 3, 4]
3. Error
4. [4]

answer: `2. [1, 2, 3, 4]`
*(Because both refer to same list)*

---

**18. What is the result of this tuple operation?**

```python
t = (1, 2, 3)
print(len(t))
```

1. 2
2. 3
3. (1,2,3)
4. Error

answer: `2. 3`

---

**19. What is the output?**

```python
s = {1, 2, 3}
s.add(3)
print(s)
```

1. {1,2}
2. {1,2,3}
3. {3}
4. Error

answer: `2. {1,2,3}`
*(Sets ignore duplicates)*

---

**20. What does this filtering code print?**

```python
names = ["abi", "bala", "arun", "ram"]
x = list(filter(lambda n: n.endswith("a"), names))
print(x)
```

1. ["abi"]
2. ["bala"]
3. ["bala", "arun"]
4. ["bala"]

answer: `2. ["bala"]`

---

**21. What is the output of this dictionary code?**

```python
d = {"a": 10, "b": 20}
d["b"] = d["b"] + 5
print(d["b"])
```

1. 5
2. 20
3. 25
4. Error

answer: `3. 25`

---

**22. What is printed by the following?**

```python
student = {"name": "Avi", "scores": {"math": 75, "cs": 85}}
print(len(student))
```

1. 2
2. 3
3. 1
4. 0

answer: `1. 2`

---

**23. What will this dictionary comprehension create?**

```python
nums = [1, 2, 3]
d = {n: n*n for n in nums}
print(d)
```

1. {1:1, 2:2, 3:3}
2. {1:1, 2:4, 3:9}
3. {1:2, 2:4, 3:6}
4. [1,4,9]

answer: `2. {1:1, 2:4, 3:9}`

---

**24. What is the output?**

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
```

1. {1, 2, 3, 4, 5}
2. {3}
3. {1, 2}
4. Error

answer: `1. {1, 2, 3, 4, 5}`

---

**25. What does the following code print?**

```python
students = ["Avi", "Bala", "Charu", "Dinesh"]
result = [s.lower() for s in students if len(s) > 4]
print(result)
```

1. ["avi"]
2. ["bala", "charu"]
3. ["charu", "dinesh"]
4. ["avi", "bala", "charu", "dinesh"]

answer: `3. ["charu", "dinesh"]`
