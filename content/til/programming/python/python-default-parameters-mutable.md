---
layout: til
title: "Python Default Parameters Tripped Me Up"
date: 2017-06-03
author: Lei Ma
categories:
- programming
- basics
tags:
- Python
summary: Python default parameters might be changed with each run
references:
  - name: Default Parameter Values in Python
    link: http://effbot.org/zone/default-values.htm
---

As one might need default parameters in python functions, such as

```
def func(inp = []):
    inp.append(1)
    return inp
```
they might cause trouble. Python functions are objects of a certain identity. Every time you run it, the input `inp` changes. The consequence is that the function returns different results.

A better strategy is to use `None`. Here is an example:


```
def func(inp = None):

    if inp is None:
       inp = []

    return inp
```

For references, please read: [Default Parameter Values in Python](http://effbot.org/zone/default-values.htm).
