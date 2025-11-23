# ✅ **40 Questions: Lists, Tuples, Sets & List Comprehension**

## **A. LISTS (15 Questions)**

1. What is a list in Python? Mention any 3 characteristics.
2. Write a Python program to access elements of a list using both indexing and a loop.
3. What will be the output?

   ```python
   li = [10, 20, 30, 20, 10]
   print(li[0] is li[4])
   ```

4. Explain positive and negative indexing with an example list.
5. What is slicing? Write examples for:

   - `li[2:5]`
   - `li[:4]`
   - `li[3:]`
   - `li[::-1]`

6. What happens when slicing goes out of range? Example: `li[2:100]`.
7. What is the difference between:

   - `li = li + [40,50]`
   - `li += [40,50]`

8. Predict the output:

   ```python
   l1 = l2 = [10, 20, 30]
   l1 += [40]
   print(l1, l2)
   ```

9. Predict the output:

   ```python
   l1 = l2 = [10, 20, 30]
   l1 = l1 + [40]
   print(l1, l2)
   ```

10. Write a program to find the largest and smallest element in a list.
11. Write code to count how many times `20` appears in the list.
12. What happens when you try to access index 10 in a list of length 5?
13. Write a program to remove duplicates from a list.
14. Why are lists called _mutable_? Give an example to prove it.
15. Write Python code to concatenate two lists and then repeat the result twice.

---

## **B. TUPLES (10 Questions)**

16. What is a tuple? Mention differences between list and tuple.
17. Why are tuples called immutable? Provide an example.
18. Predict the output:

    ```python
    t = (10, [20, 30], 40)
    t[1][0] = 99
    print(t)
    ```

19. What is the need for a **single-element tuple**? Show correct syntax.
20. Write code to unpack a tuple of three values into variables.
21. What happens when you try to modify a tuple element?
22. What is tuple packing and unpacking? Give examples.
23. Write the output:

    ```python
    t = (10, 20, 30, 20)
    print(t.count(20))
    print(t.index(20))
    ```

24. What are the advantages of using tuples over lists?
25. Why can tuples be used as dictionary keys but lists cannot?

---

## **C. SETS (10 Questions)**

26. What is a set? Mention any 3 properties of sets.
27. Why are sets unordered? What is the consequence?
28. Predict the output:

    ```python
    s = {10, 20, 20, 30}
    print(s)
    ```

29. Why is `{}` not an empty set? How do you create an empty set?
30. What will happen?

    ```python
    s = {10, [20,30]}
    ```

31. Write a program to find **union**, **intersection**, **difference**, and **symmetric difference** of two sets.
32. Difference between `remove()` and `discard()` in sets.
33. Predict the output:

    ```python
    a = {1,2,3}
    b = {3,4,5}
    print(a - b)
    print(b - a)
    ```

34. Write a program to check if one set is a subset of another.
35. What is a **frozen set**? Why is it needed?

---

## **D. LIST COMPREHENSION (5 Questions)**

36. What is list comprehension? Write syntax.
37. Convert the following into list comprehension:

    ```python
    squares = []
    for x in range(1, 6):
        squares.append(x*x)
    ```

38. Create a list of even numbers from 1 to 20 using list comprehension.
39. Write list comprehension to extract vowels from a string.
40. Create a list of tuples:

    ```
    (number, number^2)
    for numbers 1 to 10
    ```
