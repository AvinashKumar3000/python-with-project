# arguments

- values or expression or variable passed to a func call is called arguments.

### 1\. Positional arguments

**Explanation:** These are the most common type of parameters. The function determines which value corresponds to which parameter based on their **position** in the function definition. The number and order of arguments passed during the function call must match the parameters.

**Rules:**

- The number of arguments in the function call must exactly match the number of positional parameters in the function definition.
- The order of arguments must be the same as the order of parameters.

<!-- end list -->

```python
def student_info(name, age):
    print(f"{name} is {age} years old.")

# 'Alice' is a positional argument for 'name'
# '25' is a positional argument for 'age'
student_info("Alice", 25)
```

---

### 2\. Keyword arguments

**Explanation:** You can explicitly name the parameters you want to assign values to during the function call. This makes the order of arguments irrelevant and improves code readability.

**Rules:**

- You must use the parameter name followed by an equals sign (`=`) to assign the value.
- You can mix positional and keyword arguments, but **all positional arguments must come before any keyword arguments**.

<!-- end list -->

```python
def student_info(name, age):
    print(f"{name} is {age} years old.")

# Using keyword arguments, so the order doesn't matter
student_info(age=25, name="Alice")
```

---