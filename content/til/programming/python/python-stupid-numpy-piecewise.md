---
layout: til
title: "Python Stupid numpy.piecewise"
date: 2015-12-04
author: Lei Ma
categories:
- programming
- basics
tags:
- Python
summary: Python Stupid numpy.piecewise
---

The `piecewise()` function in numpy is not very good. Due to the writing of the function, one wouldn't be surprised to encounter the following error,

```python
if (n != n2):
    raise ValueError(
        "function list and condition list must be the same")
```

in which `n` is the length of condition list and `n2` is the length of function list.

To avoid it, the input should always be prepared as following

```python
x = np.asarray(x)
# The following is important to avoid the weird behavior of piecewise()
if not x.shape:
    x = np.asarray([x])
```
