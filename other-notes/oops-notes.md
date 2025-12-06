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


```python

```
