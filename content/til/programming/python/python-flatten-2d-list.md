---
layout: til
title: "Flatten 2D List in Python"
date: 2019-01-23
author: Lei Ma
category:
- 'programming'
- 'basics'
tags:
- 'Python'
summary: Flatten 2D list using sum
references:
- name: How to make a flat list out of list of lists
  link: https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
---

Here is a simple way to flatten 2D list in python.

```
l = [ [1,2], [3,4], [6,7], [8, 9,10] ]
sum( l, [] )
```

This will result in
```
[1, 2, 3, 4, 6, 7, 8, 9, 10]
```

Why is this even working?

The function `sum(an_iterable_object)` will simply use the operator `+` for the iterable object that was passed on to it. I can take in an optional parameter, i.e.,

```
sum(a_iterable_object, where_should_the_summation_start)
```

The operations would be like this:

```
result = where_should_the_summation_start or 0

for i in an_iterable_object:
   result = result + i
```

Suppose we have a nested list `[ [1,2,3], [4,5] ]`, for each iteration, sum would simply concat the sublists together.

And, this is much faster than list comprehensions.

```
%%timeit
sum( l, [] )
# 309 ns ± 27.4 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
```

```
%%timeit
[i for sublist in l for i in sublist]
# 588 ns ± 33.2 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
```