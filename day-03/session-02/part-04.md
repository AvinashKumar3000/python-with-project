
# **2. `datetime` Module**

The `datetime` module provides classes for working with dates, times, and timestamps.

- **Importing**

```python
import datetime
```

---

## **Working with Dates**

- **1. Current Date**

```python
today = datetime.date.today()
```

- **2. Creating a Date**

```python
d = datetime.date(2025, 2, 18)
```

- **3. Accessing Components**

```python
today.year
today.month
today.day
```

---

## **Working with Time**

```python
t = datetime.time(14, 30, 50)
print(t.hour, t.minute)
```

---

## **Working with Date & Time (`datetime.datetime`)**

- **1. Current Date and Time**

```python
now = datetime.datetime.now()
```

- **2. Creating a datetime Object**

```python
dt = datetime.datetime(2025, 1, 1, 10, 30)
```

---

## **Formatting and Parsing**

- **1. Format datetime → String (`strftime`)**

```python
now.strftime("%d-%m-%Y %H:%M:%S")
```

| Format | Meaning      |
| ------ | ------------ |
| %d     | Day          |
| %m     | Month        |
| %Y     | Year         |
| %H     | Hour (24-hr) |
| %M     | Minute       |
| %S     | Second       |

- **2. Parse String → datetime (`strptime`)**

```python
datetime.datetime.strptime("18-02-2025", "%d-%m-%Y")
```

---
