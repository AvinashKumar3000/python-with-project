# Tuple and Immutability

## TUPLE

- Tuple is represented using `()`.
- Insertion order is preserved.
- Duplicates are allowed.
- Heterogeneous elements are allowed.
- **Tuples are immutable** → once created, elements cannot be changed.
- Faster than list (performance-wise).
- Used for fixed data (ex: coordinates, database records).

```python
t = (10, 20, 30, 20, 30, 10)
print(t[0])
print(t[4])
print(t[0] is t[5])  # True for small integers (because of interning)
```

---

### Tuple Indexing

```
positive index        0   1   2   3   4   5
elements             10  20  30  20  30  10
negative index       -6  -5  -4  -3  -2  -1
```

Examples:

```python
t[0]
t[3]
t[-1]
t[-4]
```

Boundary checking is done for indexing (same as list).

---

## Access Elements in Tuple

```python
i = 0
while i < len(t):
    print(t[i])
    i = i + 1

for item in t:
    print(item)
```

---

## Slicing Tuples

Slicing works exactly like list slicing.

```
positive index        0   1   2   3   4   5   6   7
elements             10  20  30  40  50  60  70  80
negative index       -8  -7  -6  -5  -4  -3  -2  -1
```

Syntax: `t[start:end]`  
(start → inclusive, end → exclusive)

Examples:

- `t[2:6]`
- `t[-6:6]`
- `t[2:200]` (no boundary check in slicing)
- `t[6:2]` → `[]`
- `t[2:]`
- `t[:6]`
- `t[:]` → entire tuple

---

## Step in Tuple

Syntax: `t[start : end : step]`

Examples:

- `t[2:6:2]`
- `t[6:2:-1]`
- `t[::-1]`
- `t[::-2]`
- `t[:4:-1]`
- ❌ `t[2:6:0]` → step cannot be 0

---

## Tuple is Immutable

Once created, a tuple **cannot be modified**.

```python
t = (10, 20, 30)
t[1] = 99  # TypeError (cannot modify)
```

But:

- Inside a tuple, if there is a **mutable object** (like a list), that object can be changed.

```python
t = (10, [20, 30], 40)
t[1][0] = 200  # Allowed
print(t)       # (10, [200, 30], 40)
```

Tuple immutability applies **only to the tuple structure**, not to mutable elements inside it.

---

## Tuple Packing & Unpacking

### Packing

```python
t = 10, 20, 30
print(t)  # (10, 20, 30)
```

### Unpacking

```python
a, b, c = (10, 20, 30)
print(a, b, c)
```

### Swapping (uses tuple internally)

```python
x, y = 10, 20
x, y = y, x
print(x, y)  # 20 10
```

---

## Single Element Tuple

```python
t = (10)     # NOT a tuple, just a number
t = (10,)    # tuple
```

Comma makes it a tuple.

---

## Tuple Concatenation

```python
t1 = (10, 20)
t2 = (30, 40)
t3 = t1 + t2
print(t3)  # (10, 20, 30, 40)
```

---

## Repetition

```python
t = (10, 20)
t2 = t * 3
print(t2)  # (10, 20, 10, 20, 10, 20)
```

---

## Why Tuple is Immutable?

- Improves performance (faster than list)
- Safer (cannot change accidentally)
- Hashable → can be used as **dictionary keys** and in **sets**
- Useful for fixed datasets (constants, coordinates, config values)

---

## Tuple vs List (Quick Comparison)

| Feature          | List          | Tuple                    |
| ---------------- | ------------- | ------------------------ |
| Mutability       | Mutable       | Immutable                |
| Representation   | `[]`          | `()`                     |
| Performance      | Slower        | Faster                   |
| Allowed elements | Heterogeneous | Heterogeneous            |
| Can modify?      | Yes           | No                       |
| Can be dict key? | No            | Yes (if fully immutable) |

## tuple methods

Tuples have **only 2 built-in methods** because they are **immutable**.

---

## ✅ `tuple.count(value)`

Returns how many times a value appears in the tuple.

```python
t = (10, 20, 30, 20, 20, 40)
t.count(20)   # 3
t.count(100)  # 0
```

---

## ✅ `tuple.index(value, start=0, end=len(tuple))`

Returns the **first index** where the value appears.

Raises **ValueError** if the value is not found.

```python
t = (10, 20, 30, 20, 40)

t.index(20)      # 1
t.index(20, 2)   # 3 (search from index 2)
t.index(30)      # 2
```

```python
t.index(99)      # ValueError: tuple.index(x): x not in tuple
```

---

## 🎯 Additional Built-in Functions (Useful with Tuples)

Although not methods, these work with tuples:

### `len(t)`

Returns number of items.

### `min(t)`, `max(t)`

Works if tuple contains comparable elements.

### `sum(t)`

Works only for numeric tuples.

### `sorted(t)`

Returns a **new list** (not a tuple).

### `any(t)`, `all(t)`

Boolean checks.
