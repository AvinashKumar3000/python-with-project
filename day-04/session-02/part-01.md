# numpy

Here is a **clean, compact, beginner-friendly NumPy Cheat Sheet** — perfect for students and quick revision.

---

# 🔥 **NumPy Cheat Sheet (Python)**

---

# ✅ **1. Importing NumPy**

```python
import numpy as np
```

---

# ✅ **2. Creating Arrays**

### **From Python list**

```python
arr = np.array([1, 2, 3])
```

### **2D Array**

```python
arr = np.array([[1, 2], [3, 4]])
```

### **Zeros, Ones, Full**

```python
np.zeros((3,3))
np.ones((2,2))
np.full((2,2), 7)
```

### **Range**

```python
np.arange(0, 10, 2)   # start, stop, step
```

### **Linspace**

```python
np.linspace(1, 5, 5)  # 5 evenly spaced numbers
```

---

# ✅ **3. Array Attributes**

```python
arr.shape     # dimensions
arr.ndim      # number of dimensions
arr.size      # total elements
arr.dtype     # data type
```

---

# ✅ **4. Reshaping & Flattening**

```python
arr.reshape(3, 2)
arr.flatten()       # convert to 1D
```

---

# ✅ **5. Indexing & Slicing**

```python
arr[0]          # first element
arr[1, 2]       # row 1, column 2
arr[:, 1]       # all rows, col 1
arr[0:2, :]     # rows 0 to 1
```

---

# ✅ **6. Mathematical Operations**

### **Element-wise**

```python
arr + 2
arr * 3
arr1 + arr2
arr1 * arr2
np.sqrt(arr)
np.exp(arr)
np.log(arr)
```

### **Aggregate**

```python
np.sum(arr)
np.mean(arr)
np.max(arr)
np.min(arr)
np.std(arr)
```

---

# ✅ **7. Matrix Operations**

```python
np.dot(a, b)        # matrix multiplication
a.T                 # transpose
np.linalg.inv(a)    # inverse
np.linalg.det(a)    # determinant
```

---

# ✅ **8. Concatenation**

```python
np.concatenate([a, b])
np.vstack([a, b])   # vertical stack
np.hstack([a, b])   # horizontal stack
```

---

# ✅ **9. Boolean Filtering**

```python
arr[arr > 5]        # filter values
arr[(arr > 3) & (arr < 10)]
```

---

# ✅ **10. Random Numbers**

```python
np.random.rand(3, 2)        # random floats
np.random.randint(1, 10, 5) # random integers
np.random.randn(3, 3)       # normal distribution
```
