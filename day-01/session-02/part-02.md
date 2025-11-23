# function

## `built in function`

- print, input, range
- usage of range function
  - syntax -> `range(x,y,z)`
  - `list(range(x,y,z))`
  - `sum()` `min()` `max()`

### `user defined function`

we can create our own function

```python
def fn(x,y,z):  # func definition  ( arguments )
    pass
fn(10,20,30)       # func call        ( parameters)
```

---

calling function within function

```python
def fn1():
    print("inside fn1 start")
    print("inside fn1 end")

def fn2():
    print("inside fn2 start")
    fn1()
    print("inside fn2 end")

fn1()
fn2()
```

why to use functions

```python
a,b = 10,20
c = a+b

a,b = 12,26
c = a+b

a,b = 2,20
c = a+b

# make a code reusable
def add(a,b):
    return a+b

res = add(10,20)
print(res)
```

### return

```python

def fn1():
    return 10

val = fn1()
print(val)

def fn2():
    return 10,20

a,b = fn2()
print(a,b)

```

## lambda

to use short representation of funtion

```python
def add(a,b):
    return a+b

res = add(10,20)
print(res)

# convert to lambda
```

## What if a function not return anything ?

- then by default it return `None`
