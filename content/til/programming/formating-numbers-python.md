---
layout: til
title: "Formatting Numbers in Python"
date: 2016-10-11
author: Lei Ma
comments: true
category:
- programming
tags:
- Python
summary: Formatting numbers in python using format
references:
  - name: PyFormat
    link: https://pyformat.info/
---


`.format()` is a good way to format numbers. A good reference is [PyFormat](https://pyformat.info/).

For example, we can use scientific notation.

```python
print "{:e}".format(9887.2)
```

will give us

```
9.887200e+03
```

A quick and minimal version of what has been said is

1. ``{:04.2f}`` means make the total length of the number 4, with 2 significance digits and using 0's to fill up the other slots if the number is not long enough.
2. It's not necessary to put in all the specifications.
3. `d`, `f`, `e` can be used.
4. The signs can be speficied using `+`, e.g.,
   ```
   `{:+d}`.format(42)
   ```
