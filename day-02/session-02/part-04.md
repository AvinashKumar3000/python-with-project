# **Dictionary Comprehension**

Dictionary comprehension is the **short-hand / compact way** to create a dictionary using a **single line**.

It is similar to **list comprehension**, but it produces a **dictionary**.

---

## ✅ **Syntax**

```
{ key_expression : value_expression  for item in iterable }
```

Optional:

```
{ key : value  for item in iterable  if condition }
```

---

# **Basic Examples**

## **1. Create a dictionary of numbers and squares**

```python
d = {x : x*x for x in range(1,6)}
print(d)
```

Output:

```
{1:1, 2:4, 3:9, 4:16, 5:25}
```

---

## **2. Convert a list into a dictionary (index → element)**

```python
li = ["apple", "banana", "cherry"]
d = {i : li[i] for i in range(len(li))}
print(d)
```

Output:

```
{0:'apple', 1:'banana', 2:'cherry'}
```

---

# **Using Conditions**

## **3. Select only even numbers**

```python
d = {x : x*x for x in range(10) if x % 2 == 0}
```

Output:

```
{0:0, 2:4, 4:16, 6:36, 8:64}
```

---

## **4. Filter dictionary using comprehension**

```python
marks = {"Avi":45, "Kumar":80, "Ravi":60}
passed = {k:v for k,v in marks.items() if v >= 50}
```

Output:

```
{'Kumar':80, 'Ravi':60}
```

---

# **Modifying Values in Existing Dictionary**

## **5. Increase all marks by 5**

```python
marks = {"Avi":45, "Kumar":80, "Ravi":60}
updated = {k : v + 5 for k, v in marks.items()}
```

---

## **6. Change all values to upper case**

```python
data = {"name":"avi", "city":"coimbatore"}
upper = {k : v.upper() for k, v in data.items()}
```

---

# **Comprehension with Conditions on Values**

## **7. Tag students pass/fail**

```python
marks = {"Avi":35, "Kumar":80, "Ravi":60}
result = {k : ("Pass" if v>=50 else "Fail") for k,v in marks.items()}
```

---

# **Nested Expressions**

## **8. Reverse keys and values**

```python
d = {"a":1, "b":2, "c":3}
rev = {v : k for k,v in d.items()}
```

---

## **9. Nested loop comprehension**

**Multiplication pairs**

```python
pairs = {(x,y) : x*y for x in range(1,4) for y in range(1,4)}
```

---

# **Comprehension with String Processing**

## **10. Count character frequency using comprehension**

```python
name = "banana"
freq = {ch : name.count(ch) for ch in set(name)}
```

---

# **Comprehension + if/else inside value**

```python
nums = {x : ("Even" if x%2==0 else "Odd") for x in range(1,11)}
```

---

# **Dictionary Comprehension Summary Table**

| Purpose              | Example                                                |
| -------------------- | ------------------------------------------------------ |
| Normal comprehension | `{x:x*x for x in range(5)}`                            |
| With condition       | `{x:x*x for x in range(10) if x%2==0}`                 |
| From list            | `{i:li[i] for i in range(len(li))}`                    |
| From dict (modify)   | `{k:v+5 for k,v in d.items()}`                         |
| Reverse dict         | `{v:k for k,v in d.items()}`                           |
| Nested loops         | `{(x,y):x*y for x in A for y in B}`                    |
| Conditional value    | `{k:"Pass" if v>=50 else "Fail" for k,v in d.items()}` |
