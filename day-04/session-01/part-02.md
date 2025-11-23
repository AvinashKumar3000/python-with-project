# constructor

```python
# constructor
# instance variable
class Dog:
    breed = "german-sheperd"
    def __init__(self, name, age):
        self.name = name
        self.age = age
d1 = Dog("shiro",5)
d2 = Dog("scooby",10)

# --------------------------------------------------
#  Things to be known before proceeding.
#
#   - HOW TO ACCESS variables / methods
#     [IMPORTANT] using dot(.)

#   - class variables are common to all objects.
#   - can be accessed using, "self", "object", "class_name"
#
#   - instance variables are unique to its object.
#   - can be accessed using, "self", "object"

#   [ NOTE ] : self is nothing but refers to object.

print(d1.breed, d1.name, d1.age)
print(d2.breed, d2.name, d2.age)
print(Dog.breed)
# print(Dog.name) # not possible because,
#    name, age is a instance variable, only access by instance.
```

    german-sheperd shiro 5
    german-sheperd scooby 10
    german-sheperd

```python

```
