# loop

### while

```python
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1 

col = 5
row = 5
c = 1
while col <= 5: # outer while 
    r = 1
    while r <= r-c: # inner while
         print(b, end=" ")
         b = b + 1
    print()
    a = a + 1
    
```

---

### for

In Python, a `for` loop allows you to repeat a block of code a specific number of times. When using `range()`, you can control how many times the loop will run.

#### Syntax

```python
for variable in range(start, stop, step):
    # code to repeat
```

- **`start`** (optional): The number where the loop starts (default is 0).
- **`stop`** (required): The number where the loop stops. This is not included in the loop.
- **`step`** (optional): The amount the loop counter increases by after each iteration (default is 1).

##### Example 1: Basic Loop with `range(stop)`

```python
for i in range(5):
    print(i)
```

**Explanation**:

- The loop starts at `0` and ends at `4` (since `5` is not included).
- Output:

  ```
  0
  1
  2
  3
  4
  ```

##### Example 2: Loop with `range(start, stop)`

```python
for i in range(2, 6):
    print(i)
```

**Explanation**:

- The loop starts at `2` and ends at `5` (because `6` is not included).
- Output:

  ```
  2
  3
  4
  5
  ```

##### Example 3: Loop with `range(start, stop, step)`

```python
for i in range(0, 10, 2):
    print(i)
```

**Explanation**:

- The loop starts at `0`, ends at `8` (since `10` is not included), and increments by `2` each time.
- Output:

  ```
  0
  2
  4
  6
  8
  ```

##### Example 4: Loop in Reverse with `range()`

```python
for i in range(5, 0, -1):
    print(i)
```

**Explanation**:

- The loop starts at `5`, ends at `1`, and decreases by `1` each time.
- Output:

  ```
  5
  4
  3
  2
  1
  ```

---

---

### break

- break keyword will only work inside
- the for, while ( loops )

```python
# some other examples
a = 1
while a <=10:
    print(a)
    if a == 4:
        break
    a = a + 1

# some other examples
# example - 01
a = 1
while a <=10:
    print(a)
    if a == 4:
        break
    a = a + 1
else:
    print("loop completed") 

# example - 02
a = 1
while a <=10:
    print(a)
    a = a + 1
else:
    print("loop completed") 
```

```python
# find prime no
n = int(input())
i = 2
isPrime = True
while i<(n**0.5):
    if n%i == 0:
        isPrime = False
        break
    i = i + 1

if isPrime:
    print("is Prime")
else:
    print("is not a Prime")

# find prime no
n = int(input())
i = 2
while i<(n**0.5):
    if n%i == 0:
        print("Not a prime")
        break
    i = i + 1
else:
    print("is a Prime")

# NOTE: If break executed, then else not get executed.


```

---

### continue

- continue keyword will only work inside
- the for, while ( loops )

diff `continue` and `break` in Python:

| **Concept**   | **`break`**                                 | **`continue`**                            |
|---------------|---------------------------------------------|-------------------------------------------|
| **Purpose**   | Exits the loop entirely.                    | Skips the current iteration and moves to the next. |
| **Effect**    | Terminates the loop when executed.          | Skips the remaining code in the current iteration, but the loop continues. |
| **When to use**| When you want to stop the loop early.       | When you want to skip certain iterations but continue looping. |
| **Example use**| Exiting a loop when a condition is met.     | Skipping an iteration based on a condition. |

#### Example using `continue` and `break` together

```python
for i in range(10):
    if i == 3:
        continue  # Skip when i is 3
    if i == 8:
        break  # Exit the loop when i is 8
    print(i)
```

**Explanation**:

- The loop prints numbers from `0` to `9`.
- When `i` is `3`, `continue` skips the rest of the code for that iteration, so `3` is not printed.
- When `i` is `8`, `break` terminates the loop, so `8` and anything beyond it are not printed.

**Output**:

```
0
1
2
4
5
6
7
```

---

---

### pass

    In Python, the `pass` statement is a placeholder that does nothing. It’s used when a statement is syntactically required but you don’t want to execute any code. Typically, you use `pass` in situations where you plan to add code later or you want to skip a block without causing errors.

#### Common Uses of `pass`

1. **Empty Function or Class**: You can use `pass` when you want to define a function or class but aren’t ready to implement the logic yet.
2. **Placeholders in Conditional Statements**: Sometimes in `if`, `for`, or `while` statements, you may want to skip certain conditions temporarily.

#### Example 1: `pass` in Conditional Statements

```python
for i in range(5):
    if i == 3:
        pass  # Do nothing when i is 3
    else:
        print(i)
```

**Output**:

```
0
1
2
4
```

In this example, when `i` is `3`, the `pass` statement is executed, meaning the loop does nothing for that iteration, but continues with the next.

---