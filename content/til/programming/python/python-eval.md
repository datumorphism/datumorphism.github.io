---
layout: til
title: "eval in Python is Dangerous"
date: 2019-08-13
author: Lei Ma
category:
- programming
- basics
tags:
- Python
summary: eval is powerful but really dangerous
---

`eval` in python will try to execute the strings as python code.

Consider the following python code,

```python

import os

__cwd__ = os.getcwd()
__location__ = os.path.realpath(
    os.path.join(__cwd__, os.path.dirname(__file__))
    )

print(f'location: {__location__}')
print(f'filename: {__file__}')

with open(os.path.join(__location__, __file__),'r') as fp:
    content = fp.read()

print(content)

exec(content)
```

The code will execute the content of the file itself.

{{< repl url="https://repl.it/@emptymalei/Python-eval-in-code?lite=true" >}}
