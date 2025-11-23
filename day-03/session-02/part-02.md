
## `raise exception`

### Purpose

- Used to manually raise an exception.
- Useful for handling error conditions and custom error reporting.

<img src="./raise example (1).png">

<img src="./raise example (2).png">

#### example 01

```python
def fn(x,y):
    if y==0:
        raise ValueError("💀 ZERO Is not possible 💀")
    return x/y 

print(fn(1,0))
```

#### example 02

```python
def calculate_square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return x ** 0.5

try:
    result = calculate_square_root(-5)
except ValueError as e:
    print(e)  # Output: Cannot calculate square root of a negative number
```

## `User-defined-exception`

### Basic Points on User-Defined Exceptions in Python

- User-defined exceptions used to create custom exception
- This can make your error handling more easy
- And your code more readable.

#### Key Points

1. **Purpose**:
   - Provide more meaningful error messages.
   - control over exception handling.

2. **Defining a Custom Exception**:
   - Create a new class that inherits from the built-in `Exception` class or any of its subclasses.

3. **Syntax**:

   ```python
   class MyCustomError(Exception):
       pass
   ```

4. **Raising a Custom Exception**:
   - Use the `raise` keyword to raise the custom exception.

   ```python
   raise MyCustomError("This is a custom error message")
   ```

5. **Catching a Custom Exception**:
   - Use a `try-except` block to handle the custom exception.

   ```python
   try:
       # Code that may raise MyCustomError
       raise MyCustomError("An error occurred")
   except MyCustomError as e:
       print(e)
   ```

6. **Example**:

   ```python
   class NegativeNumberError(Exception):
        pass

   def check_positive(number):
       if number < 0:
           raise NegativeNumberError(number)
       return number

   try:
       check_positive(-5)
   except NegativeNumberError as e:
       print(e)
   ```

   - **Defining the Exception**: `NegativeNumberError` inherits from `Exception` and includes a custom message.
   - **Raising the Exception**: The `check_positive` function raises `NegativeNumberError` if the input number is negative.
   - **Catching the Exception**: The `try-except` block catches the custom exception and prints the error message.