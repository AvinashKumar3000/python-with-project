# **Basic Notes on Python Object-Oriented Programming (OOP)**

**Key Concepts:**

- **Class:**
  - A blueprint for creating objects.
  - It defines the properties (attributes) and behaviors (methods) of objects.
  - Tips to remember:
    - A dog has 4 legs, 2 ears, 2 eyes, shape, color. These are (properties/attributes) of dog.
    - sound, running speed, etc actions are (methods/behaviors)
    - attributes : subject
    - methods : actions
- **Object:**
  - An instance of a class.
  - It has its own unique set of attributes.
  - And can perform the actions defined by the class's methods.
- **Inheritance:**
  - The process of creating new classes (child classes) from existing classes (parent classes).
  - Child classes inherit the attributes and methods of their parent classes.
- **Polymorphism:**
  - The word "polymorphism" means "many forms. where "poly" means "many" and "morphism" means "forms".
  - Polymorphism is the ability of an objects of different types to respond to the same method call in different ways.
- **Encapsulation:**
  - process of binding attributes and methods together into single entity.

- **Abstraction**
  - Hiding important data and only showing necessary data is called abstraction.

```python
# DISCLAIMER : python not supports fully object oriented programming language.

# how to create a class in Python.
# - using class keyword
# - basically, the class name mostly starts with the first letter.
class Sample:
    pass
class Animal:
    pass

```

```python
# How to create an object
# - object is also called as instance
class Sample:
    pass

obj1 = Sample()
obj2 = Sample()

# --------------------------------------------

class Ship:
    pass
black_pearl = Ship()
titanic = Ship()
# black_pearl and titanic is an object
```

```python
# functions in Python class are called methods
```

```python
# How to declare methods inside a class
#  3 types of methods in class
#     - instance method
#     - class method
#     - static method
class Sample:
    def __init__(self): # special method, called constructor,   By default we have make constructor as instance method.
        pass            # executes while object is creating.
        
    def fn1(self): # instance method    : only access by objects/instance
        pass

    @classmethod
    def fn2(cls):     # class method       : can access by class. which mean common to all objects.
        print(cls)
        
    @staticmethod
    def fn3():        # static method      : considrcommon to object
        pass
```

```python
# 2 types of variables in class
# - class variable
# - instance variable

class Sample:
    v2 = 100 # class variable
    def __init__(self,v1): 
        self.v1 = v1 # instance variable
        
    def fn1(self,a,b): 
        print(a+b+self.v1)
       
    @classmethod
    def fn2(cls,x,y):     
        print(x*y*cls.v2)
        
    @staticmethod
    def fn3(a,b,c):        
        print(a+b+c)

obj = Sample(10)
obj.fn1(2,3)
obj.fn2(2,3)
obj.fn3(1,2,3)

print("-----------------------------------------")

# Sample.fn1(2,3) # ERROR: as need an object/instance to call instance method.
Sample.fn2(2,3)
Sample.fn3(1,2,3)
# How output came.
```

    15
    600
    6
    -----------------------------------------
    600
    6
    

```python
# How to declare the variables in class
#  2 types of variables in class
#     - instance variable
#     - class variable
class Sample:
    b = 123 # class variable : created inside class
            #  common to all objects.
    def fn(self):
        # You can create variables in any functions.
        # Mostly they are created inside function.
        self.a = 10   # instance variable  : created using lass_name

```
