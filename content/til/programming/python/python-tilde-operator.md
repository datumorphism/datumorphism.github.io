---
layout: til
title: "Python Tilde Operator"
date: 2019-08-15
author: Lei Ma
categories:
- programming
- basics
tags:
- Python
references:
  - name: 'The tilde operator in Python @StackOverflow'
    link: https://stackoverflow.com/questions/8305199/the-tilde-operator-in-python/8305291
summary: tilde operator may not work as you expected
---

`~` in python will invert the value. The actual method depends on the implementation of `__invert__` method of the argument.

Let's start with the numbers.

```python
~10 # -11
~-10 # 9

~1 # -2
~-1 # 0

~0 # -1
```

The case for `True` and `False`

```python
~True # -2
~False # -1

# which are the same as
~1 # -2
~0 # -1
```

