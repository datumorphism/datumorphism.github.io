---
layout: til
title: "Copy Scalars and Lists in Python"
date: 2018-07-03
author: Lei Ma
category:
- programming
- basics
tags:
- Python
excerpt: Python copy values of scalars but addresses of lists
---

Python allows copying values of a scalar:

```
a = 42
b = a
print(b)
# 42

a = 43
print(a)
# 43
print(b)
# 42
```

However, the same operator `=` doesn't do the same for lists:
```
a = [1,2,3]
b = a
print(b)
# [1,2,3]

a[1] = 0
print(a)
# [1,0,3]
print(b)
# [1,0,3]
```
The reason is quite easy to guess. The variable `a` and `b` for lists are pointers since it is much easier to hold the starting address of the lists and length instead of all the values.

In the case of a copy of a list is really needed, we can use slicing:
```
a = [1,2,3]
b = a[:]
```
Through this slicing, `b` is a copy of `a` and all changes of `a` have no effect on `b`.

