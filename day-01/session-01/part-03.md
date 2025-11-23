# data types

## `comment`

- where to use, Consider a scenario where you don't want to execute a line of codes.
- The developers uses comments that will restrict the execution of such code.
- Some times, developers use comments to explain written codes.

```python
a = 10 # a is assigned with value 10
b = 20
# In below code 
# - we are doing addition operation
# - and storing in variable c
c = a + b
print(c)
```

- why in python we use # for comments
- why not `//` for comments | in c, cpp, java, javascript we use `//` for comments
- because already `//` has been used for `floor division`

---

### `Data types`

```md
     Data types
       /      \
  Numeric    string datatype
  /                \
int               str
float
bool
complex     
```

    In python, we don't have following datatypes
        - char
        - double
    - the size of the datatype is dependent on the 
      virtual memory of the system.

#### `int`

1. +ve, =ve, 0 are called `int`
1. size/range is dependent on machine

```python
# some times you want to store money information in code
amount = 1,00,000 # 1 lakh
print(amount) # (1,0,0)

# you can make above code readable by using underscore.
amount = 1_00_000
print(amount) # 100000
# 💡NOTES:
# - only point is, use underscore(_) in-between the digits
# - not in front or rear of digits.

>>> 123 # valid
>>> _123 # invalid
>>> 1_23 # valid
>>> 12_3 # valid

# underscore, ["_"] can be used anywhere it is supported 
# but it is only our wish to make use of it in a meaningful
# way
# - we use it to represent huge number for readability
```

- you can represent binary, octal, hexadecimal in integer

```python
# you can use both small and capital letters ( b, B, x, X, o, O )
a = 0b1010 # (or) 0B1010
print(a) # 10
b = 0o10 # (or) 0O10
print(b) # 8
c = 0xA  # (or) 0XA
print(c) # 10

>>> 00001 
# above code is invalid, 
# because, in int, prefix 0 is already used for number representation.
# we can't use like above code. it will through error.

# print function will always by default return the decimal value. 
```

#### `float`

- float data will only follow "decimal representation"
- `0b10.10` is wrong becase, here this is meaning less,
  - and in python you can use 0b, 0B, 0x, 0X, 0o, 0O in integer type only.
- `1e3` mean `1*10**3`, 1 multiple of 10 to power of 3
- float will follow only "decimal representation"
- we can represent, binary, octal, hexadecimal in float
- Hence `>>> a = 00001.32` is a valid code.

```python
# rare examples
# below is actually type conversion
>>> float("inf") 
inf
>>> float("-inf")
-inf
>>> float("-inf") * 10
-inf
>>> float("nan")
nan
>>> float("infinity")
inf

# in python we can represent infinite like this.
```

#### `boolean`

- boolean is a subset of integer
- It has 2 vales
- Those are `True` and `False`,
- Where first letter `T` and `F` is capital.
- Internally `True` has value `1`
- and `False` has value `0`

#### `complex`

- This is all about complex numbers which comes under subject `math`
- examples of valid complex numbers
  - `5+3j`
  - `5-3j`
  - `3j`
  - `5+3J`
  - `3.5+3J`
  - `3.5+6J`
  - `0b1010 + 21j`
  - `0x13 + 0x13J`

```python
a = 7 + 9j
print(a.real) # 7.0
print(a.imag) # 9.0
```

```python
# - complex internally uses `float`.
# - Eg, 
>>> S= 100 + 3j
>>> S.real
100.0 # which is a float
>>> S.imag
3.0   # which is a float
>>> type(S.real)
<class 'float'>
```

```python
v1 = 4 + 5j
v2 = 6 + 3j
print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 / v2)
print(v1 // v2) # ERROR 💀. can use // in complex 
```

#### `strings`

- in python there is no data type like 'char' ( character )
- Because in c, cpp we have a data type called 'char'
- In python we can create/represent string in following ways.
  - pair of single quotes `'`
  - pair of double quotes `"`
  - triple quotes
    - pair of 3 single quotes `'''`
    - pair of 3 double quotes `"""`

Before proceeding, learn 2 function ord() and chr()

- `chr()` function can convert ordinance to character
- `ord()` function can convert character to ordinance.
- Here ordinance is nothing but `asciii` character.

```python
>>> ord("A") # 65
>>> ord('A') # 65
>>> ord("ABC") # ERROR
# so you can send only string of length 1.
```

```python
# chr() function is used to convert an integer to it's
# character based on the unicode.
>>> chr(65) # 'A'
>>> chr(97) # 'a'
>>> chr(0x101) # 'ā'
# range allowed in chr function is as below
# 0 to 1114111
>>> chr(-1) # ERROR
# negative values are not allowed.
```

##### raw string

- raw string are the one.
- where it will not take escape sequences characters.

```python
>>> s1 = 'hello \n world`
>>> print(s1)
hello 
world
>>>
# above is the output.

## now i want to store \n as characters
# instead of escape sequence.
# to do that we will use raw string.
# - simple add r or R in front of strings.
>>> s1 = r"hello \n world"
>>> print(s1)
hello \n world
```

##### usual string

```python
# valid ways to create a string in python
a = 'h'
a = "h"
a = "hello"
a = "" # empty string
a = " " # a single space in string
a = '''line 1
line 2
line 3
line 4
''' # we use triple quotes to store string in that can 
# be written in multiple lines
a = "don't" # outside - " and inside - '
a = 'I will never "give up"' # outside - ' and inside - "
a = 'hai\nhello\twhat\'\"\\' # these are escape sequences
```

---

`ADDITIONAL NOTES`

##### REPL

REPL stands for Read-Eval-Print Loop. It is an interactive programming environment that takes user inputs (one at a time), evaluates them, and returns the result to the user. This process is repeated in a loop, hence the name "Read-Eval-Print Loop."

### `comparison operators`/`relational operator`

#### types

- Equality `== !=`
- Relational `> < >= <=`
- Membership `in     not in`
- Identity `is       is not`
- always above operators will return result in True/False

---

- `==` Equal To
- `!=` Not Equal To
- `>` Greater Than
- `<` Less Than
- `>=` Greater Than or Equal To
- `<=`  Lesser Than or Equal To
- `in` # checks if given item in sequence
- `not in` # checks if given item not in sequence
- `is` # check if left content `id` is same as right `id`
- `is not` # check if left content `id` is not same as right `id`
- `NOTE :` # we cannot do comparison on complex types.

##### `Lexicographical comparison`

```python
# this means, you can compare strings in python
# How this is working ? 🤔 
# - It will compare each characters ASCII value
print( 'abc' == 'abc' ) # True
print( 'abc' == 'bbc' ) # False
print( 'abc' <= 'bbc' ) # True

>>> 'h' <= 'A' # False
# if s1 > s2 is True, then s1 should come after s2
# if s1 > s2 is False, then s1 should come before s2

"hello" > "hell" # True
"hell" > "hello" # False
"hello" > "hello" # False
"hello" >= "hello" # True
"cab" >= "bac" >= "abc" # True
" " >= " " # True
```

```python
>>> 6 >= 3 <=1 == 1 <=5 >= True >=0 <= 8
False
# we go from  left to right
# every argument is evaluated only once
# if truth hood is decided as "False" then rest of expression is not executed.
# 
```

###### `membership operator`

- in, not in => works on iteration in strings.

```python
>>> s1 = "welcome"
>>> print("co" in s1)
True
>>> "oc" in s1
False
>>> 'c' in s1
True
>>> 'com' in s1
True
>>> 'on' in s1
False
```

```python
>>> s1 = "welcome to everyone"
>>> 'to' in s1
True
>>> 'too' in s1
False
>>> 'is' not in s1
True
>>> 'one' in s1
True
>>> 'T' in s1
False
```

```python
>>> a = 100
>>> 1 in a
# because int is not an iterable.
# iterables example, 
# list, strings, tuple
```

### MUTABLE AND IMMUTABLE

- Immutable Objects are of in-built datatypes like int, bool, string, Unicode, and tuple. In simple words, an immutable object can’t be changed after it is created.
- Mutable Objects are of type Python list, Python dict, or Python set. Custom classes are generally mutable.
- The content in the object cannot be changed.
- if we are trying to change, then a new object will be created with that contents.

    note:
  - creating n no of objects with the same content is a stupid activity. hence to save memory, we create only one object and all references all pointing to same object.
  - if one reference is trying to change the content.in the object, other objects will have impact.
  - To overcome this problem, content in the object should be modified. This concept is called immutable.
  - If any person is trying to change the content in the immutable object, then a new object is created with new content.
  - 📝 In python, everything is a object (i,e) every variable
  - Here we have a function called id() => hashcode(address)
  - which provides the address of the variable.

---

`is`

- is operator is used to check if a variable are pointing to same object.
- is is used to compare reference (or) addresses (or) hashcode.

|`is`  |`===`  |
|---------|---------|
|Meant for reference comparison    | Meant for content comparison         |
|It is used to check both references (or) pointing to same object or not    | It is used to check both the content or value is same or not         |

```python
# for int
# only following range will have same id by default
# range : -5 to 256
>>> a = 10
>>> b = 10
>>> a == b
True
>>> a is b
True
>>> id(a), id(b)
(140730277624536, 140730277624536)
----------------------------------------
>>> a = 10.12
>>> b = 10.12
>>> a == b
True
>>> a is b
False
>>> id(a), id(b)
(1184823356912, 1184823356336)
----------------------------------------
>>> a = 10.12
>>> b = a
>>> a == b
True
>>> a is b
True
>>> id(a)
3215396023792
>>> id(b)
3215396023792

```