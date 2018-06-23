---
layout: til
title: "Python Default Parameters Tripped Me Up"
date: 2017-06-03
author: OctoMiao
category:
- programming
- basics
tag:
- Python
excerpt: Python default parameters might be changed with each run
---

As we might use default parameters in python functions, such as

```
def func(inp = []):
    inp.append(1)
    return inp
```

this might cause trouble. Since python functions are objects of a certain identity no matter how many times you run it, the input `inp` would be changed with each run.

The better strategy is to use `None`.


```
def func(inp = None):

    if inp is None:
       inp = []

    return inp
```


For references, please read: [Default Parameter Values in Python](http://effbot.org/zone/default-values.htm).
