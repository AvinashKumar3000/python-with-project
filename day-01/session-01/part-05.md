## `logical operators`

- `and`
- `or`
- `not`

---

`and`

    arg1 and arg2
    * arg1 is non-zero then result is arg2
    * arg1 is 0 then result is arg1

```python
# example
>>> 5 and 10
10
>>> 100 and 0
0
>>> True and False
False
>>> 3.75 and 6.42
6.42
>>> 0 and 100
0
>>> 0 and 0
0
>>> "hello" and "hai"
'hai'
>>> False and True
False
>>> False and False
False
>>> " " and "hai"
'hai'
```

---

`or`

    arg1 or arg2
    * arg1 is non-zero then result is arg1
    * arg1 is 0 then result is arg2

```python
>>> 10 or 5
10
>>> 7 or 0
7
>>> 6.5 or -5
6.5
>>> False or 100
100
>>> False or False
False
>>> 0 or 2.5
2.5
```

- In case of `and` 1st is `0` don't go next.
- In case of `or` 1st is non-zero then don't go for next.

---

`not`

```python
# not True -> False
# not False -> True
# not non-zero => False
# not zero -> True
# not 10 -> False
# not 3.5 -> False
# not False -> True

# in below code, 
# == has high priority
# but 10==not is invalid.
>>> a = 10 == not 100
  File "<stdin>", line 1
    a = 10 == not 100
              ^^^
SyntaxError: invalid syntax

>>> 10 != (not 100)
True
>>> not 10 == 0
True
>>> not 100 and 20
False
>>> 10 and not 20
False
>>> 0 and not 100
0
# last scenario, as first it is zero.
# python will not check further.
```

---

```python
# mostly we use logical operators 
# - to compare multiple conditions like
a = 10
b = 20
c = 30
if not ( a>b and b>=c or a==c ):
   print('condition satisfied')
```

```python
>>> 10 and 20 and 0 and 100 and 200
0
>>> 10 and 20 and [] and 20 and (1,2)
[]

# in above cases. It will convert each and every thing into its boolean type then evaluates. Once it stop evaluation it will through the ans. 
# 10 -> bool(10)  -> True
# 20 -> bool(20)  -> True
# [] -> bool([])  -> False
# 20 -> bool(20)  -> True

# As we are using only `and`. Python will stop once it gets 
# False ( bool([]) -> False ).
# so only we got output as `[]`
```

---

## type of errors

|syntax error  |Runtime error  |
|---------|---------|
|No output at all     |   runs some code, stop where ever there is a problem     |

- python script is executed from top to bottom, ( controlling is also possible )
- python will follow a rule called indentation
- every statement should be under a indentation
- default indentation is main indentation

```python
# indentation error
print("A")
   print("B") # this will come under "main indentation"
# indentation error comes under syntax error, so no output.
```

```python
a = 10 # we mentioned to python that, we are going to use a.
print(a + b) # error, because, b is not yet defined.
# we didn't told to python, that we are using "b"
```

---

## `Flow control`

### if

```python
print("A")        # main indentation/block
print("B")        # main indentation/block
if True:          # main indentation/block
    print("C")        # IF indentation/block
    print("D")        # IF indentation/block
print("E")        # main indentation/block
print("F")        # main indentation/block
```

#### if syntax

- if keyword followed by condition,
- where condition can be an valid expression, or variable or anything
- that can be converted to boolean.
- Python finally checked if it is True or False.
  - if is True. then executes IF block
  - if is False. then executes ELSE Block

```python
# some invalid indentation codes.

# code 01
print(10)
if (3>2):
    print(20)
  print(30) # this will not comes under either main/if block.
print(40)

# code 02
print(10)
if (3>2):
   print(20)
      print(30) # this will not comes under either main/if block.
print(40)

# code 03
print(10)
if (3>2): # expected an indented block after 'if' statement
print(20)
print(30) 
print(40)
```

some if code scenario's

```python
# code 01
print(10)
if (3>2):
    pass # this is used, when you don't want to write a code now. 
    # but you will write in future.
    # pass will do nothing. 
print(20)
print(30)
print(40)

# code 02
print(10)
if (): # empty brackets are always valid, 
    # is consider False, 
    # Because it means, empty tuple.
    print(20)
print(30)

# code 03
print(10)
if :# End up with syntax error. 
    # Because, bracket is mandatory
    print(20)
print(30)
```

---

### else

```python
# WAP to find max of 2 numbers
a = int(input())
b = int(input())
if a > b:
    res = a 
else:
    res = b
print(res)

# alternate solution
a = int(input())
b = int(input())
res = (a>b)*a + (b>a)*b
print(res)
```

```python
# some valid indentation codes.

# code 01
print(10)
if (3>2):
    print(20)    # this will comes under if block
    print(25)
else:
          print(26)
          print(30) # this will not comes under either else block.
print(40)

# 💡In python switch concept is not there.💡 
# But later match is introduced...
# But now we can use elf for doing switch logic.
key = input() # W A S D
if key == "W":
    print("move forward")
elif key=="S":
    print("move backward")
elif key == "A":
    print("move left")
elif key == "D":
    print("move right")
else: # it is optional to write else here.
    print("invalid key")
```


### conditional operator

- is a concept used, literally a short form of if else
- Technically we can call it as "conditional expression"
- But it act as an expression

```python
a = int(input())
b = int(input())
res = a if a > b else b
print(res)

# syntax 
#   a            if         a > b        else           b
#  [True res] [if keyword] [ condition] [else keyword] [False res]
# to put in simple terms.
# res1 if exp else res2

    
```