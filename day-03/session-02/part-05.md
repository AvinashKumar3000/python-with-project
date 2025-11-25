
# **3. `os` Module**

The `os` module provides functions for interacting with the operating system, especially file and directory management.

---

## **Common `os` Functions**

- **1. Get Current Working Directory**

```python
import os
os.getcwd()
```

- **2. Change Directory**

```python
os.chdir("C:/Users/")
```

- **3. List Items in a Directory**

```python
os.listdir()
```

- **4. Create a Directory**

```python
os.mkdir("new_folder")
```

- **5. Create Nested Directories**

```python
os.makedirs("a/b/c")
```

- **6. Delete a File**

```python
os.remove("data.txt")
```

- **7. Remove Directories**

```python
os.rmdir("myfolder")      # only if empty
os.removedirs("a/b/c")    # removes nested structure
```

- **8. Check if a Path Exists**

```python
os.path.exists("file.txt")
```

- **9. Join Paths Correctly**

```python
os.path.join("folder", "file.txt")
```

- **10. Get File Size**

```python
os.path.getsize("myfile.txt")
```