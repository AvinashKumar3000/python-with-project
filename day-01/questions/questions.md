# **`DAY 01` QUESTIONS**

---

## **1. Which of the following is a valid variable name in Python?**

1. _student1
2. student-1
3. 1student
4. student 1

answer: `1. _student1`

---

## **2. What is the data type of the value `.0` in Python?**

1. int
2. float
3. str
4. invalid

answer: `2. float`

---

## **3. What will be stored in variable `x`?**

```python
x = int("10.5")
```

1. 10
2. 10.5
3. Error
4. None

answer: `3. Error`

---

## **4. What will this code print?**

```python
print("Hello" "Python")
```

1. HelloPython
2. Hello Python
3. ("Hello", "Python")
4. Error

answer: `1. HelloPython`

---

## **5. What does this expression return?**

```python
print(10 == 10.0)
```

1. False
2. True
3. Error
4. Depends on version

answer: `2. True`

---

## **6. What will the following loop print?**

```python
for i in range(1, 4):
    print(i, end="-")
```

1. 1-2-3-4-
2. 1-2-3-
3. 0-1-2-
4. 1 2 3

answer: `2. 1-2-3-`

---

## **7. Which of the following correctly defines a function with no parameters?**

1. def fun
2. def fun():
3. function fun():
4. fun() => {}

answer: `2. def fun():`

---

## **8. What will be the output?**

```python
x = 3
if x == 3:
    print("One")
elif x == 3:
    print("Two")
else:
    print("Three")
```

1. One
2. Two
3. Three
4. Error

answer: `1. One`

---

## **9. What is the output of the function?**

```python
def calc(a, b=2):
    return a * b

print(calc(5))
```

1. 10
2. 7
3. Error
4. 5

answer: `1. 10`

---

## **10. What will this loop print?**

```python
i = 3
while i >= 0:
    i -= 1
print(i)
```

1. 0
2. -1
3. 1
4. None

answer: `2. -1`

---

## **11. How many times will the inner print execute?**

```python
for i in range(3):
    for j in range(i):
        print("Hi")
```

1. 1
2. 2
3. 3
4. 4

answer: `3. 3`

---

## **12. What is printed by this code?**

```python
def fun(a, b, c=5):
    return a + b * c

print(fun(2, 3))
```

1. 21
2. 17
3. 15
4. 2 + 3 * 5

answer: `2. 17`

---

## **13. What is the output?**

```python
n = 6
flag = True
for i in range(2, n):
    if n % i == 0:
        flag = False

print(flag)
```

1. True
2. False
3. Error
4. None

answer: `2. False`

---

## **14. What does this Fibonacci code print?**

```python
a, b = 1, 1
for _ in range(4):
    print(b)
    a, b = b, a + b
```

1. 1 1 2 3
2. 1 2 3 5
3. 0 1 1 2
4. 1 1 1 1

answer: `2. 1 2 3 5`

---

## **15. What will this recursion output?**

```python
def fun(n):
    if n == 1:
        return 1
    return n + fun(n-1)

print(fun(4))
```

1. 4
2. 6
3. 10
4. 16

answer: `3. 10`

---

## **16. What does this code calculate?**

```python
marks = [60, 70, 80]
total = 0
for m in marks:
    total += m
avg = total / len(marks)

if avg > 75:
    grade = "A"
else:
    grade = "B"

print(total, grade)
```

1. 210 A
2. 210 B
3. 70 A
4. 70 B

answer: `2. 210 B`

---

## **17. What does this code do?**

```python
num = 13
for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")
```

1. Always prints Prime
2. Always prints Not Prime
3. Checks if number is prime
4. Checks even number

answer: `3. Checks if number is prime`

---

## **18. What is the output?**

```python
for i in range(3, 6):
    for j in range(6 - i):
        print("*", end="") 
    print(end=" ")
```

1. `***  **  *`
2. `* * * * * *`
3. `* ** ** *`
4. `******`

answer: `1. ***  **  *`

---

## **19. What will this function return?**

```python
def mystery(n):
    if n <= 2:
        return n
    return mystery(n-1) * mystery(n-2)

print(mystery(4))
```

1. 2
2. 4
3. 6
4. 8

answer: `2. 4`

---

## **20. What is the output?**

```python
x = 0
for i in [1, 2, 3]:
    x = x + i
print(x)
```

1. 6
2. 3
3. 1 2 3
4. Error

answer: `1. 6`

---

## **21. What does this program compute?**

```python
marks = [50, 70, 80, 90]
total = 0
for m in marks:
    total += m

avg = total / len(marks)

print(avg > 70)
```

1. True
2. False
3. Depends on input
4. Error

answer: `1. True`

---

## **22. What will this code print?**

```python
print(type(10 / 5))
```

1. `<class 'int'>`
2. `<class 'float'>`
3. `<class 'number'>`
4. Error

answer: `2. <class 'float'>`

---

## **23. What is the output of the loop?**

```python
for i in range(1, 4):
    if i == 2:
        continue
    print(i, end="")
```

1. 123
2. 13
3. 12
4. 23

answer: `2. 13`

---

## **24. What does this function return?**

```python
def test(a, b):
    return a if a > b else b

print(test(5, 9))
```

1. 5
2. 9
3. True
4. False

answer: `2. 9`

---

## **25. What is the final value of `x`?**

```python
x = 1
for i in range(3):
    x = x * (i + 1)
print(x)
```

1. 1
2. 2
3. 6
4. 3

answer: `3. 6`
