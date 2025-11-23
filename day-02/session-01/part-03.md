# SETS & SET OPERATIONS

## SET

- Set is represented using `{}` or `set()`.
- **Unordered** → no index, no slicing.
- **Duplicates are NOT allowed**.
- **Heterogeneous elements allowed**.
- **Mutable** → but elements must be immutable (hashable).
- Automatically removes duplicates.
- Faster for membership checking (`in`, `not in`).

```python
s = {10, 20, 30, 20, 10}
print(s)   # {10, 20, 30}
```

---

## Creating Sets

### Normal set

```python
s = {10, 20, 30}
```

### Empty set (IMPORTANT)

```python
s = {}        # this is NOT a set → it is a dict
s = set()     # correct
```

### Heterogeneous elements

```python
s = {10, 3.14, "python", True}
```

### Invalid element (mutable)

```python
s = {10, [20, 30]}  # TypeError (list is unhashable)
```

---

## Basic Operations

### Add element

```python
s.add(40)
```

### Remove element

```python
s.remove(20)    # removes 20, error if not found
s.discard(50)   # no error if 50 not found
```

### Pop element (random)

```python
s.pop()
```

### Clear set

```python
s.clear()
```

---

## Mathematical Set Operations

Let:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

### 1. **Union** → elements from both sets

```python
a | b
a.union(b)
# {1, 2, 3, 4, 5, 6}
```

---

### 2. **Intersection** → common elements

```python
a & b
a.intersection(b)
# {3, 4}
```

---

### 3. **Difference** → a minus b

```python
a - b
a.difference(b)
# {1, 2}

b - a
# {5, 6}
```

---

### 4. **Symmetric Difference**  
Elements in either set but not in both

```python
a ^ b
a.symmetric_difference(b)
# {1, 2, 5, 6}
```

---

## Update Operations (in-place modifications)

```python
a.update(b)                  # union update
a.intersection_update(b)     # intersection update
a.difference_update(b)       # difference update
a.symmetric_difference_update(b)
```

---

## Membership

```python
10 in s
50 not in s
```

---

## Set Comprehension

```python
s = {x*x for x in range(1,6)}
print(s)   # {1, 4, 9, 16, 25}
```

---

## Frozen Set (Immutable Set)

```python
fs = frozenset([10, 20, 30])
fs.add(40)    # ❌ error (immutable)
```

- Hashable  
- Can be used in dictionary keys  
- Supports all set operations except modification

---

## Properties of Set (Quick Summary)

- Unordered  
- No indexing  
- No slicing  
- No duplicate elements  
- Mutable (but elements must be immutable)  
- Very fast for membership checking  
- Supports full mathematical set operations  
- Frozen set gives immutability  

---

## Common Set Methods (Cheat Sheet)

| Method | Description |
|--------|-------------|
| `add()` | Add element |
| `remove()` | Remove (error if not found) |
| `discard()` | Remove (no error) |
| `pop()` | Remove random element |
| `clear()` | Empty set |
| `union()` | Combine sets |
| `intersection()` | Common elements |
| `difference()` | Elements in A not B |
| `symmetric_difference()` | Unique elements only |
| `update()` | In-place union |
| `intersection_update()` | In-place intersection |
| `difference_update()` | In-place difference |
| `symmetric_difference_update()` | In-place symmetric difference |
| `issubset()` | Check subset |
| `issuperset()` | Check superset |
| `isdisjoint()` | Check no common elements |
