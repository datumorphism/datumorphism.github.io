---
layout: til
title: "matplotlib x y limit and aspect ratio"
date: 2016-07-21
author: Lei Ma
categories:
- programming
- basics
tags:
- Python
- Matplotlib
summary: matplotlib x y limit and aspect ratio
---

Use

```
plt.xlim(-1,1)
plt.gca().set_aspect('equal', adjustable='box')
```

if

```
plt.xlim(-1,1)
plt.axes().set_aspect('equal', 'datalim')
```

doesn't work.
