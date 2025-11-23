# ✅ **Python Polymorphism — Complete Notes**

## **1. What is Polymorphism?**

**Polymorphism** means _one thing, many forms._

In Python:

- The **same function name** can work in **different ways** depending on the object.
- It increases flexibility and reduces repeated code.

---

# 🟦 **2. Types of Polymorphism in Python**

Python supports:

### **2.1. Duck Typing**

“If it walks like a duck and quacks like a duck, it is a duck.”

Python does **not** check the type, only checks if the object has the required method.

### **2.2. Method Overriding (Runtime Polymorphism)**

A child class gives its **own version** of a method already present in the parent class.

### **2.3. Operator Overloading**

Same operator behaves differently depending on the object.

### **2.4. Function Overloading (Not directly supported)**

But can be achieved using:

- default parameters
- variable arguments (`*args`)

---

# 🟩 **3. Duck Typing Example**

```python
class Dog:
    def sound(self):
        return "Woof"

class Cat:
    def sound(self):
        return "Meow"

def make_sound(animal):
    print(animal.sound())

make_sound(Dog())
make_sound(Cat())
```

➡ Same function (`make_sound`) works for both Dog and Cat — polymorphism.

---

# 🟧 **4. Method Overriding (Runtime Polymorphism)**

```python
class Vehicle:
    def start(self):
        print("Vehicle starting...")

class Car(Vehicle):
    def start(self):
        print("Car engine starting...")

v = Vehicle()
c = Car()

v.start()
c.start()
```

➡ Child class `Car` overrides parent method.

---

# 🟨 **5. Operator Overloading**

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

a = Number(10)
b = Number(20)

print(a + b)   # uses __add__()
```

➡ The `+` operator behaves differently for `Number` objects.

---

# 🟪 **6. Function Overloading (Python style)**

Python overwrites the last defined function, so to achieve overloading:

```python
def add(a, b=0, c=0):
    return a + b + c

print(add(10))       # 10
print(add(10, 20))   # 30
print(add(10, 20, 30))  # 60
```

➡ Same function name, different usage.

---

# 🟫 **7. Polymorphism with Class Methods**

```python
class Shape:
    def area(self):
        pass

class Square(Shape):
    def area(self):
        return "Area of square"

class Circle(Shape):
    def area(self):
        return "Area of circle"

for obj in (Square(), Circle()):
    print(obj.area())
```

---

# 🟰 **8. Why is Polymorphism Important?**

✔ Reduces duplicate code
✔ Makes programs flexible
✔ Supports OOP design
✔ Allows writing universal functions

---

# 🟩 **9. Summary Table**

| Type                 | Meaning                          | Example               |
| -------------------- | -------------------------------- | --------------------- |
| Duck Typing          | Method depends on object         | `sound()` for Dog/Cat |
| Method Overriding    | Child replaces parent method     | `Car.start()`         |
| Operator Overloading | Same operator, different meaning | `__add__()`           |
| Function Overloading | Same function, different params  | `add(a,b,c)`          |
