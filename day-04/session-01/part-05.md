# encapsulation

1. What is Encapsulation?

Encapsulation means wrapping data and methods into a single unit (class) and restricting direct access to the data.

It helps in:

- protecting data
- controlling how data is accessed
- preventing accidental changes


```python
# access specifiers

class Parent:
    a = 10     # public    :  can access in class, subclass, object
    _b = 20   # protected :   can access in class, subclass
    __c = 30 # private   :    can access in class
    def __init__(self):
        print(self.a)
        print(self._b)
        print(self.__c)
class Child(Parent):
    def __init__(self):
        super().__init__()
        print(self.a)
        print(self._b)
        # print(self.__c) # not accessable
obj = Child()
print(obj.a)
print(obj._b) # still accessable. as python partially implements oops concept
# print(obj.__c) # not accessable
```

    10
    20
    30
    10
    20
    10
    20

```python
class Account:
    def __init__(self):
        self.__balance = 0   # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = Account()
acc.deposit(500)
print(acc.get_balance())
```
