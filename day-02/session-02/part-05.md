# 🔥 20 Python Dictionary Interview Questions

1. **What is a dictionary in Python? How is it different from a list?**

2. **Are dictionary keys ordered or unordered in Python?**
   _(Before and after Python 3.7)_

3. **What are the rules for dictionary keys?**

   - Can we use a list as a key? Why/why not?

4. **What happens if you try to access a key that does not exist?**

   - How is `dict.get()` different from `dict[key]`?

5. **How do you loop through keys, values, and items in a dictionary?**

6. **What is the difference between `del`, `pop()`, and `popitem()`?**

7. **How does `update()` work?**

   - What happens if a key already exists?

8. **Why is dictionary lookup fast?**
   _(Hint: Hashing)_

9. **How to merge two dictionaries in Python?**

10. **Explain dictionary comprehension with an example.**

11. **How do you remove all items from a dictionary?**

    - What happens to references?

12. **What does `dict.setdefault()` do?**

    - Give an example.

13. **Can dictionaries have duplicate values?**

    - Can they have duplicate keys? Explain with example.

14. **How to sort a dictionary by:**
    a) key
    b) value

15. **How to invert (reverse) a dictionary?**
    Convert `{a:1, b:2}` → `{1:a, 2:b}`.

    - What if values are not unique?

16. **What is `fromkeys()`?**

    - Explain with example.

17. **What is the difference between `==` and `is` when comparing dictionaries?**

18. **How to create nested dictionaries?**

    - How do you access inner values?

19. **What will be the output?**

```python
d = {}
d[1] = "A"
d[True] = "B"
print(d)
```

_(Hint: `1` and `True` have the same hash.)_

20. **Write a Python expression to count the frequency of elements in a list using a dictionary.**

Example list:

```python
li = [1, 2, 2, 3, 3, 3]
```
