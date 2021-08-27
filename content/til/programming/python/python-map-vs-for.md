---
layout: til
title: "Python Map vs For in Python"
date: 2015-12-04
author: Lei Ma
categories:
- 'programming'
- 'basics'
tags:
- Python
summary: Python Map vs For in Python
---



`map` is sometimes more convenient instead of for. The code

```python
newlist = []
for word in oldlist:
    newlist.append(word.upper())
```

can be reformed using `map`

```python
newlist = map(str.upper, oldlist)
```

`for` loop is sometimes slow because the dot evaluation inside is evaluated for each loop. Thus the following code is more efficient.

```python
upper = str.upper
newlist = []
append = newlist.append
for word in oldlist:
    append(upper(word))
```
