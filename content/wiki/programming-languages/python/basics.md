---
title: "The Python Language: Basics"
description: "Python as a programming language"
date: 2018-03-20
toc: true
category:
- 'Programming Language'
tag:
- 'Python'
- 'Programming Language'
- 'Basics'
references:
- name: "Superfunction"
  link: "http://www.pythonforbeginners.com/super/working-python-super-function"
weight: 101
---


## Numbers, Arithmetics

Two types of numbers exist,

1. int
2. float, 15 digits, other digits are float error

It is worth noting that in Python 2, we have

```python
print(1.0/3)
# will give us float numbers
# 0.333333333333
```

while

```python
print(1/3)
# will only give us int
# 0
```

However, this was changed in Python 3.


## Variables, Functions, Conditions


A variable name should start with either a letter or an underscore.

Variables defined inside a function is local and there is no way to find it or use it outside the function. It is even possible to reuse an already used global variable inside a function.


```python
# num1 is a global variable

num1 = 1
print(num1)

# num2 is a local variable

def fun():
    num1 = 2
    num2 = num1 + 1
    print(num2)

fun()
```

where the first line will give us 1 but the second output is 3. (Code from Coursera course interactivepython-005/lecture/15.)

If we want to use the global variable and change the value of it, the program can be like this,

```python
num = 4

def fun1():
    global num
    num = 5

def fun2():
    global num
    num = 6

# note that num changes after each call with no obvious explanation
print(num)
fun1()
print(num)
fun2()
print(num)
```

from Coursera course interactivepython-005/lecture/15.

Start a function by a comment says what the function does.

```python
def triangle_area(base, height):     # header - ends in colon
    area = (1.0 / 2) * base * height # body - all of body is indented
    return area                      # body - return outputs value
```

from Coursera course interactivepython-005/lecture/8.

`:` indicates that a block code is following, which should be indented.

```python
# will return True if a year is a leap year on Mars
def is_leap_year(year):
    if year % 3000 == 0:
        return False
    elif year % 1000 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif (year % 2 == 0) and (year % 10 == 0):
        return True
    else:
        return False
```



## Zen Code


1. https://www.python.org/doc/essays/list2str/



### Filter, Map, and List Comprehension


`filter()`, `map()`, `reduce()`, and list comprehension: `link to code <https://repl.it/@emptymalei/Python-filter-map-reduce>`_


<iframe height="400px" width="100%" src="https://repl.it/@emptymalei/Python-filter-map-reduce?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>



## Super function


In python you can access parent class properties easily.

```python
class MyParentClass(object):
    def __init__(self):
        pass

class SubClass(MyParentClass):
    def __init__(self):
        MyParentClass.__init__(self)
```

To access the sub class properties, we can use super function.

```python
class MyParentClass():
    def __init__(self):
        pass

class SubClass(MyParentClass):
    def __init__(self):
        super()
```