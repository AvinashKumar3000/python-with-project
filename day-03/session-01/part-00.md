# pre requirements

## **Opening Files**

| Mode   | Meaning             | Usage                 |
| ------ | ------------------- | --------------------- |
| `"r"`  | Read (default)      | File must exist       |
| `"w"`  | Write               | Overwrites file       |
| `"a"`  | Append              | Adds new data at end  |
| `"x"`  | Create              | Error if file exists  |
| `"r+"` | Read + Write        | File must exist       |
| `"w+"` | Write + Read        | Overwrites            |
| `"a+"` | Append + Read       | Creates if not exists |
| `"b"`  | Binary mode         | `"rb"`, `"wb"`        |
| `"t"`  | Text mode (default) | `"rt"`, `"wt"`        |

### **Syntax**

```python
file = open("sample.txt", "r")
```

## **Closing Files**

```python
file.close()
```

## **Best Method → Using `with` (Auto-close)**

```python
with open("sample.txt", "r") as f:
    data = f.read()
```

## **Reading Files**

### **Read entire file**

```python
f.read()
```

### **Read first N characters**

```python
f.read(10)
```

### **Read one line**

```python
f.readline()
```

### **Read all lines as list**

```python
f.readlines()
```

### **Iterating line-by-line**

```python
for line in f:
    print(line)
```

---

## **Writing to Files**

### **Write string**

```python
f.write("Hello")
```

### **Write multiple lines**

```python
f.writelines(["A\n", "B\n", "C\n"])
```

## **Appending to File**

```python
with open("data.txt", "a") as f:
    f.write("New line\n")
```

---

## **Check if File Exists**

```python
import os

os.path.exists("data.txt")
```

---

## **File Pointer Methods**

### **Get current position**

```python
f.tell()
```

### **Move file pointer**

```python
f.seek(0)      # Move to beginning
f.seek(5)      # Move to index 5
```

## **Delete a File**

```python
import os
os.remove("sample.txt")
```

---

## **Working with JSON Files**

### **Write JSON**

```python
import json

with open("data.json", "w") as f:
    json.dump({"name": "Avi"}, f)
```

### **Read JSON**

```python
with open("data.json", "r") as f:
    data = json.load(f)
```

---

## **Working with CSV Files**

### **Write CSV**

```python
import csv

with open("test.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
```

### **Read CSV**

```python
import csv

with open("test.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

---

## **Binary File Handling**

### Write binary

```python
with open("img.jpg", "wb") as f:
    f.write(b"binarydata")
```

### Read binary

```python
with open("img.jpg", "rb") as f:
    data = f.read()
```
