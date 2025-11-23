# exception handling

## Basic Notes on `try`, `except`, and `finally` in Python

Python's exception handling mechanism allows you to manage errors gracefully. The `try`, `except`, and `finally` blocks are used to catch and handle exceptions. Here's a breakdown:

### 1. `try` Block

- The code that might raise an exception is placed inside the `try` block.
- If no exceptions occur, the `except` block is skipped.

### 2. `except` Block

- This block is executed if an exception occurs in the `try` block.
- You can specify one or more exception types to handle different exceptions separately.

### 3. `finally` Block

- The `finally` block contains code that will run no matter what.
- It is executed after the `try` and `except` blocks, whether an exception occurred or not.
- It's commonly used for cleanup actions (e.g., closing files or releasing resources).

### Example

```python
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code that runs if the specific exception occurs
    print("Cannot divide by zero!")
finally:
    # Code that runs no matter what
    print("This runs no matter what.")
```

### Explanation

1. **`try` Block**: The division by zero raises a `ZeroDivisionError`.
2. **`except` Block**: Catches the `ZeroDivisionError` and prints an error message.
3. **`finally` Block**: Runs regardless of whether an exception was raised or not, ensuring that the cleanup code is executed.

### Multiple `except` Blocks

You can have multiple `except` blocks to handle different types of exceptions.

```python
try:
    value = int("abc")
except ValueError:
    print("ValueError: Invalid literal for int()")
except TypeError:
    print("TypeError: Type mismatch")
finally:
    print("Execution completed.")
```

<img src="./multi-exception-eg.png">

<img src="./multi-exception-eg02.png">

---

## `8-mark`

| **Aspect**               | **Error**                                                                                     | **Exception**                                                                              |
|--------------------------|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| **Definition**           | Errors are issues in a program that can cause it to stop running.                              | Exceptions are events that can be caught and handled within the program.                   |
| **Handling**             | Usually not handled by the program itself. The program terminates.                            | Can be handled using try-except blocks to allow the program to continue running.           |
| **Examples**             | SyntaxError, IndentationError, MemoryError                                                    | ValueError, IndexError, KeyError, ZeroDivisionError                                        |
| **Source**               | Detected before or during the execution of the program (compile-time or runtime).              | Typically detected during the execution of the program (runtime).                          |

---
