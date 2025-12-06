# oops 

- object oriented
  programming language.
- 4 pillars of oops
	- encapsulation
	- inheritance
	- polymorphism
	- abstraction

class : blueprint of an object.
object: instance of a class.

eg:
```python
class Sample:
    pass

obj = Sample()
```
##### `variable`: declared inside class
	- variables / attributes / properties / data-member
    
##### `function`: declared inside class
	- method   /  behaviours / member-function
```python
class Sample:
	a = 10
	b = 20

	def fn():    
		print("hello world")
```


```python
class Sample:
    a = 10     # data members
    b = 20
    def fn():  # member-functions
        print("function inside class")
```


```python
print(Sample.a, Sample.b)
Sample.fn()
```

    10 20
    function inside class
    

### Encapsulation
- binding of data-member and member-function together into a single entity is called encapsulation

## Inheritance
- sharing property of a parent class to a child class is called inhertiance.

#### Types of inheritance
1. single
2. multiple
3. multi level
4. heirarchical
5. hybrid


```python
class Parent:
    a = 10
    b = 20

class Child(Parent):
    c = 30
# single inheritance :
#       where once child class is inheriting from one parent
#       class is called single inheritance. 
```


```python
print(Parent.a, Parent.b)
print(Child.c)
print(Child.a, Child.b, Child.c)
```

    10 20
    30
    10 20 30
    


```python
# multiple inheritance.
#     if a single child class inheriting from multiple parent class
#     then it is called multiple inheritance.
class Parent1:
    a = 10
class Parent2:
    b = 20
class Child(Parent1, Parent2):
    c = 30
```


```python
print(Parent1.a, Parent2.b, Child.c)
print(Child.a, Child.b, Child.c)
```

    10 20 30
    10 20 30
    


```python
# multi-level inheritance.
#     level by level properties are shared between classes
#        is called multi-level inheritance. 
class A:
    a = 10
class B(A):
    b = 20
class C(B):
    c = 30
```


```python
print(A.a, B.b, C.c)
print(C.a, C.b, C.c)
```

    10 20 30
    10 20 30
    


```python
# heirarchical inheritance. 
#    when more than one child class inheriting from same parent class
#       is called heirarchical inheritance. 
class A:
    a = 10
class B(A):
    b = 20
class C(A):
    c = 30
print(C.c, C.a)
print(B.b, B.a)
```

    30 10
    20 10
    


```python
# hybrid inheritance.
#   combination of more than one type of inheritance

class A:
    a = 10
class B(A):
    b = 20
class C(A):
    c = 30
class D(B,C):
    d = 40
```


```python
print(D.a, D.b, D.c, D.d)
```

    10 20 30 40
    

# diagram for types of inheritance

```bash
single inheritance

    A --->  B 

multiple inheritance

    A     B
     \   /
      \ /
       C

multi level inheritance

        A
        |
        B
        |
        C
        
heirarchical inheritance

        A  
       / \
      /   \
     B     C

hybrid inheritance.
        A  
       / \
      /   \
     B     C
      \   /
       \ /
        D
        
```

# polymorphism 
- poly => many
- morphism => shapes
- ability of an object to respond diff for diff scenarios is called polymorphism.
  
## Types
  - over loading ( compile time polymorphism )
  - over riding  ( run time polymophism )
    

# over loading

```c
void fn(int a){
   printf("%d",a);
}
void fn(float a){
    printf("%f",a);
}
void main() {
    int x = 10;
    float y = 23.3;
    fn(x);
    fn(y);
}


```python
# overloading is not possible in python
# becuase if we create multiple func
#   with same name, then latest func will be declared.
#   all other will be omitted.
```


```python
# here in below
# python is indirectly implementing over-loading concept.
def fn(a=10,b=20,c=30):
    print(a,b,c)

fn()
fn(1)
fn(1,2)
fn(1,2,3)
```

    10 20 30
    1 20 30
    1 2 30
    1 2 3
    


```python
# over riding
#   in inheritance child class method will override
#       parent class method. that is called over-riding.

class Parent:
    def fn():
        print("Hello")
class Child(Parent):
    def fn():
        print("hi")
```


```python
Child.fn()
```

    hi
    

# abstraction
- hiding the internal implmentation
- and only showing essential information


```python
# ABC    Abstract Base Class
from abc import ABC, abstractmethod
```


```python
class Engine(ABC):
    @abstractmethod
    def start(self):
        pass
class V8(Engine):
    def start(self):
        print("engine started")
```


```python
mustang = V8()
```


```python
mustang.start()
```

    engine started
    


```python

```


```python
class Sample:
    a = 100

obj1 = Sample()
obj2 = Sample()
obj3 = Sample()
print(obj1.a)
print(obj2.a)
print(obj3.a)
Sample.a = 500
print(obj1.a)
print(obj2.a)
print(obj3.a)
```

    100
    100
    100
    500
    500
    500
    


```python
## types of variables inside class
#   - class variable
#   - instance variable
```


```python
# class variables
class Sample:
    a = 100  # class variable
    b = 200  # class variable

Sample.c = 300 # class variable
```


```python
# class var is shared to all the objects.
# u can create or manipulate class var only using class name
obj = Sample()
print(obj.a, obj.b, obj.c)
```

    100 200 300
    


```python
class Staff:
    a = 90  # class variable

lancer = Staff()
puff  = Staff()
```


```python
lancer.name= "Danny Phantom" # instance variable
puff.name = "SpongeBob" # instance variable
```


```python
puff.is_famous = True # instance variable
```


```python
dir(lancer)
```




    ['__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getstate__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     'a',
     'name']




```python
# Instance variable
##   Instance mean object.
##   Only depends upon object.
##    u can create or manipulate instance var only using an object.
```

#### types of methods
- instance method
     - associated with object.
     - only call this method with an object.
     - cannot call this method with a class.
- class method
     - associated with class.
     - can call this method with an object.
     - can call this method with a class.
- static method
     - not associated with class / object.
     - can call with both class & object.


```python
class Sample:
    def fn1(self,x,y): # instance method
        print("instance method", x+y)
    @classmethod
    def fn2(cls,x,y): # class method
        print("class method", x+y)
    @staticmethod
    def fn3(x,y):
        print("static method", x+y)
```


```python
obj = Sample()
```


```python
obj.fn1(10,20)
```

    instance method 30
    


```python
obj.fn2(10,20)
Sample.fn2(11,22)
```

    class method 30
    class method 33
    


```python
obj.fn3(10,20)
Sample.fn3(11,22)
```

    static method 30
    static method 33
    


```python

```
