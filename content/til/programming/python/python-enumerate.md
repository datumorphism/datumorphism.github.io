---
layout: til
title: "Python enumertate"
date: 2015-12-04
author: Lei Ma
categories:
- programming
- basics
tags:
- Python
summary: Python enumertate function
---

[Code Style of Python Guide](http://docs.python-guide.org/en/latest/writing/style/)

`enumerate()` can be used to keep track of the index of the list.

```python
test = [None] * 5
for n, elem in enumerate( range(5,10) ):
    print n, elem
    test[n] = elem*2
```

Here we also used the technique of creating a list of length 5.
