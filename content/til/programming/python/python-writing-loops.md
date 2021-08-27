---
layout: til
title: "Python Various Ways of Writing Loops"
date: 2015-12-04
author: Lei Ma
categories:
- 'programming'
- 'basics'
tags:
- 'Python'
summary: Python Various Ways of Writing Loops
references:
  - name: Great Python Tricks for avoiding unnecessary loops in your code
    link: http://forums.udacity.com/questions/1002566/great-python-tricks-for-avoiding-unnecessary-loops-in-your-code
---




1. List Comprehension

```python
[2*x+3 for x in list]
```


2. `map`

```python
map(function, list)
```

A function can also be defined on the fly.

```python
map(lambda x: function of x, list)
```


For multivariable,

```python
map(lambda x,y:x+y, xlist, ylist)
```


3. `zip` and `map`

`zip` is useful in a map of multivariable function.

```python
map(functionofxy, zip(xlist,ylist))
```

As given in the reference link, one good example is

```python
map(sum,zip(A,B,C))
```


4. `map` and list comprehension



```python
[map(lambda x: x+3, list) for list in shape2by2list]
```




Ref. [Great Python Tricks for avoiding unnecessary loops in your code](http://forums.udacity.com/questions/1002566/great-python-tricks-for-avoiding-unnecessary-loops-in-your-code)
