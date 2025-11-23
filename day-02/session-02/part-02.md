
# **Dictionary Identity & Mutability**

```bash
>>> d1 = {"a":1, "b":2}
>>> d2 = d1
>>> d1 is d2   # True
>>> d1["a"] = 100
>>> d1 == d2   # True
```

- Both point to **same dictionary**
- Changing one affects the other

```python
d1 = d2 = {"x":10, "y":20}
d1 is d2     # True
```

---

# **Dictionary Copying**

```python
d1 = {"a": 10, "b": 20}
d2 = d1.copy()
print(d1 is d2)  # False
```

- `.copy()` creates a **new dictionary**
- Modifying `d1` does NOT affect `d2`

---

# **Dictionary Concatenation**

❌ Not allowed

```python
d1 = {"a":10}
d2 = {"b":20}
d3 = d1 + d2   # TypeError
```

✔ Correct way:

```python
d3 = {**d1, **d2}
```

OR

```python
d1.update(d2)
```

---

# **Updating Dictionary with update()**

```python
d = {"a":10, "b":20}
d.update({"c":30, "b":200})
print(d)
```

- Existing keys are modified
- New keys are added

---

# **Deleting Items in Dictionary**

### Methods:

| Operation            | Usage        |
| -------------------- | ------------ |
| Remove by key        | `pop(key)`   |
| Remove last inserted | `popitem()`  |
| Remove specific key  | `del d[key]` |
| Clear all            | `d.clear()`  |

### Examples:

```python
d.pop("a")       # removes key=a
d.popitem()      # removes last inserted item
del d["b"]       # delete key b
d.clear()        # empty dictionary
```

---

# **Membership Operators**

```python
"name" in d
"age" in d
"salary" not in d
```

Checks only **keys**, not values.

---

# **Dictionary Methods**

```
d.keys()
d.values()
d.items()
d.get(key)
d.update({...})
d.pop(key)
d.popitem()
d.clear()
d.copy()
```

---

# **Dictionary with step-like behavior**

❌ Step/index-based slicing is NOT allowed.
Dictionary does NOT support numeric indexing.

---

