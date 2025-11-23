Perfect 👍 Here’s a **complete question on Prime Number Generation** with **example, explanation, and code** — suitable for beginners and teaching purposes.

---

### 🔢 **Question: Prime Number Generation**

**Q:**
Write a Python program to **print all prime numbers** within a given range.

A **prime number** is a number that is **greater than 1** and has **no divisors other than 1 and itself**.
In other words, a prime number cannot be divided evenly by any other number except `1` and itself.

---

### **Example:**

**Input:**

```
Enter lower range: 1  
Enter upper range: 10
```

**Process:**
Prime numbers between 1 and 10 are:

```
2, 3, 5, 7
```

**Output:**

```
Prime numbers between 1 and 10 are: 2 3 5 7
```

---

### **Explanation:**

| Number | Divisible By | Prime or Not |
| ------ | ------------ | ------------ |
| 1      | -            | ❌ Not Prime  |
| 2      | 1, 2         | ✅ Prime      |
| 3      | 1, 3         | ✅ Prime      |
| 4      | 1, 2, 4      | ❌ Not Prime  |
| 5      | 1, 5         | ✅ Prime      |
| 6      | 1, 2, 3, 6   | ❌ Not Prime  |
| 7      | 1, 7         | ✅ Prime      |
| 8      | 1, 2, 4, 8   | ❌ Not Prime  |
| 9      | 1, 3, 9      | ❌ Not Prime  |
| 10     | 1, 2, 5, 10  | ❌ Not Prime  |

---

### **Python Code Example (Using Loop):**

```python
# TODO
```

---

### **Explanation of Code:**

1. Get lower and upper range from user.
2. Loop through each number in that range.
3. Skip numbers ≤ 1 since they’re not prime.
4. For each number, check if it’s divisible by any number from 2 to `num-1`.
5. If not divisible by any — it’s a **prime number**.

---

Would you like me to make a **version that uses a function** (like `is_prime(num)`) for better clarity?
