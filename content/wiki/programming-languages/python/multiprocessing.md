---
title: "The Python Language: Multi-Processing"
description: "Python as a programming language"
date: 2018-05-10
category:
- 'Programming Language'
tags:
- 'Python'
- 'Programming Language'
- 'Basics'
references:
- name: "An introduction to parallel programming using Python's multiprocessing module"
  link: http://sebastianraschka.com/Articles/2014_multiprocessing.html
- name: Parallelism in one line A Better Model for Day to Day Threading Tasks
  link: http://chriskiehl.com/article/parallelism-in-one-line/
weight: 3
---


Python has built-in multiprocessing module in its standard library.

One simple example of using the Pool class is the following.

```python
def myfunc(myfuncargs):
    'some thing here'

with Pool(10) as p:
    records = p.map(myfunc, myfuncargs)
```

However, there are limitations on this, especially on pickles. Another approach.

```python
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

with ThreadPool(1) as p:
    records = p.map(myfunc, myfuncargs)
```

Beware that `map` function will feed in a list of args to the function. So I have to use `p.map(myfunc, [arg])` for one arg.

