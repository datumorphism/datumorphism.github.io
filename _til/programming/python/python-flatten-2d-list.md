---
layout: til
title: "Flatten 2D List in Python"
date: 2019-01-23
author: OctoMiao
category:
- 'programming'
- 'basics'
tag:
- 'Python'
excerpt: Flatten 2D list using sum
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