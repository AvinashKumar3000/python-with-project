# inheritance



```python
# ------------------
#   INHERITANCE
# ------------------

class Parent:
    a = 10
    b = 20

class Child(Parent): # by keeping parent class name in paranthesis
    pass

obj = Child()
print(obj.a)
print(Child.a)
```

    10
    10

```python
# type of inheritance
# 1. Single Inheritance: A class inherits from one superclass/Parentclass.
class Parent:
    def __init__(self):
        self.value = "Parent"

    def display(self):
        print(self.value)

class Child(Parent):
    def __init__(self):
        super().__init__() # always using this line,
        # becuase, if you not using this, parent constructor will not get called
        self.value = "Child"

obj = Child()
obj.display()  # Output: Child
```

    Child

```python
# 2. Multiple Inheritance: A class inherits from more than one superclass.
class ClassA:
    def method_a(self):
        print("ClassA method")

class ClassB:
    def method_b(self):
        print("ClassB method")

class ClassC(ClassA, ClassB):
    def __init__(self):
        pass
obj = ClassC()
obj.method_a()  # Output: ClassA method
obj.method_b()  # Output: ClassB method

```

    ClassA method
    ClassB method

```python
# 3. Multilevel Inheritance: A class inherits from a superclass, which itself inherits from another superclass.
```

```python
class Grandparent:
    def __init__(self):
        self.grandparent_value = "Grandparent"

class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        self.parent_value = "Parent"

class Child(Parent):
    def __init__(self):
        super().__init__() # you have to use this. if you want to call parent class constructor.
        # if not, python will only call child constructor.
        #
        self.child_value = "Child"

obj = Child()
print(obj.grandparent_value)  # Output: Grandparent
print(obj.parent_value)       # Output: Parent
print(obj.child_value)        # Output: Child

```

    Grandparent
    Parent
    Child

```python
# 4. Hierarchical Inheritance: Multiple classes inherit from the same superclass.
class Parent:
    def __init__(self):
        self.value = "Parent"

class Child1(Parent):
    pass

class Child2(Parent):
    pass

obj1 = Child1()
obj2 = Child2()
print(obj1.value)  # Output: Parent
print(obj2.value)  # Output: Parent

```

    Parent
    Parent

```python
# 5. Hybrid Inheritance: A combination of two or more types of inheritance.
class ClassA:
    def method_a(self):
        print("ClassA method")

class ClassB(ClassA):
    def method_b(self):
        print("ClassB method")

class ClassC:
    def method_c(self):
        print("ClassC method")

class ClassD(ClassB, ClassC):
    pass

obj = ClassD()
obj.method_a()  # Output: ClassA method
obj.method_b()  # Output: ClassB method
obj.method_c()  # Output: ClassC method

```

    ClassA method
    ClassB method
    ClassC method

```python

```

```python

```

```python

```
