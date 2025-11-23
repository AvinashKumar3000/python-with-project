# **Dictionary Operations and Methods**

## **DICTIONARY**

- Dictionary is represented in `{key : value}`.
- Insertion order is preserved (Python 3.7+).
- Keys must be **unique**.
- Values can be **duplicates**.
- Heterogeneous keys and values are allowed.
- Keys must be **immutable** (string, number, tuple).

```python
d = {"a": 10, "b": 20, "c": 30, "b": 200}
print(d["a"])
print(d["b"])
print(d["c"])
```

- Keys are unique → second `"b"` overrides the first.

---

`d = {"id":101, "name":"Avi", "age":26, "city":"Coimbatore"}`

### **Accessing Elements in Dictionary**

There is **no indexing** (like list).
We use **keys** to access values.

```
keys:     "id"   "name"   "age"   "city"
values:    101    Avi      26      Coimbatore
```

### Examples:

```python
d["id"]
d["name"]
d["age"]
d["city"]

d.get("age")
d.get("salary")   # None
```

⚠️ When using `d[key]`, **key must exist**, otherwise → `KeyError`.

---

## **Traversing the Dictionary**

```python
# keys
for k in d:
    print(k)

# values
for v in d.values():
    print(v)

# both key & value
for k, v in d.items():
    print(k, v)
```

---

# **Slicing**

❌ **Dictionary does NOT support slicing.**
Because dictionary does **not have index positions**.

---

# **Adding & Modifying Elements**

```
keys:     "id"   "name"   "age"   "city"
values:    101    Avi      26      Coimbatore
```

```python
d = {"id":101, "name":"Avi"}

# Add new key-value pair
d["age"] = 27

# Modify existing key
d["name"] = "Avinash"
```

- If key exists → value updates
- If key does not exist → new pair is added

---
