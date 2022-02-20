---
title: Three dots in Python
description: 'Use three dots as placeholder for python empty function'
date: 2020-12-03
authors:
  - LM
categories:
  - programming
  - basics
tags:
  - Python
links:
  - wiki/programming-languages/python/basics.md
updated: '2020-12-03'
---


Using three dots in Python:

```python
from abc import abstractmethod

class A:
    def __init__(self):
        self.name = "A"
        print("Init")

    def three_dots(self): ...

    @abstractmethod
    def abs_three_dots(self): ...

    def raise_it(self):
        raise Exception("Not yet done")



a = A()

print("\nthree_dots")
print(a.three_dots())

print("\nabs_three_dots")
print(a.abs_three_dots())

print("\nraise_it")
a.raise_it()
```

Returns

```
three_dots
None

abs_three_dots
None

raise_it
Traceback (most recent call last):
  File "main.py", line 27, in <module>
    a.raise_it()
  File "main.py", line 14, in raise_it
    raise Exception("Not yet done")
Exception: Not yet done
```


{{< repl url="https://repl.it/@emptymalei/threedotsinpython?lite=true" >}}


