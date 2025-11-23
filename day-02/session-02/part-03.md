
# **Important Concept: = vs update()**

```python
d1 = {"a":10}
d2 = d1

d1.update({"b":20})
print(d1)
print(d2)
```

Both change because both refer to same dictionary.

But:

```python
d1 = {"a":10}
d2 = d1
d1 = d1 | {"b":20}   # Creates a new dictionary
```

- `d1` becomes new dictionary
- `d2` remains old dictionary

Exactly same logic as:

- `a = a + x` creates new object
- `a += x` modifies existing object

---

# **Practical Examples**

---

## **1. Count character frequency**

```python
name = "banana"
count = {}

for ch in name:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print(count)
```

---

## **2. Student Marks Dictionary**

```python
marks = {"math":90, "science":80, "english":70}

total = sum(marks.values())
avg = total / len(marks)

print("Average:", avg)
```

---

## **3. Nested Dictionary**

```python
college = {
    "s1": {"name":"Avi", "age":26},
    "s2": {"name":"Kumar", "age":22}
}

print(college["s1"]["name"])
```

---

## **4. Filter Dictionary**

```python
marks = {"Avi":40, "Kumar":90, "Ravi":55}

passed = {k:v for k,v in marks.items() if v >= 50}
print(passed)
```

---
