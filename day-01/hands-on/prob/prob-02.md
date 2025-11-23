# 🌀 **Question: Fibonacci Series**

**Q:**
Write a Python program to print the **Fibonacci series** up to `n` terms.

The Fibonacci series is a sequence of numbers where:

* The **first two terms** are `0` and `1`.
* Every next term is found by **adding the two previous terms**.

The formula is:
[
F(n) = F(n-1) + F(n-2)
]

---

### **Example:**

**Input:**

```
Enter number of terms: 7
```

**Process:**
Fibonacci sequence starts as:

```
0, 1, 1, 2, 3, 5, 8
```

**Output:**

```
Fibonacci series: 0 1 1 2 3 5 8
```

---

### **Explanation:**

| Term | Calculation | Result |
| ---- | ----------- | ------ |
| F(0) | –           | 0      |
| F(1) | –           | 1      |
| F(2) | F(1) + F(0) | 1      |
| F(3) | F(2) + F(1) | 2      |
| F(4) | F(3) + F(2) | 3      |
| F(5) | F(4) + F(3) | 5      |
| F(6) | F(5) + F(4) | 8      |

---

### **Python Code Example (Using Loop):**

```python
# TODO
```

---

### **Explanation of Code:**

1. `a` and `b` start with 0 and 1 — the first two terms.
2. The loop runs `n` times.
3. Each time, print the current number (`a`).
4. Then update the values:

   * `a` becomes the previous `b`,
   * `b` becomes the sum of `a + b`.

---

Would you like me to generate the **recursion-based Fibonacci question** next (for advanced learners)?
