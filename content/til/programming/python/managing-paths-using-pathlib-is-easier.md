---
title: "Managing path using pathlib in Python"
description: "It is a convinient package to manage path and files"
date: 2021-07-15
authors:
  - "LM"
categories:
  - "programming"
tags:
  - "Python"
  - "os"
references:
  - name: "pathlib — Object-oriented filesystem paths"
    link: "https://docs.python.org/3/library/pathlib.html"
  - name: "# Why you should be using pathlib"
    link: "https://treyhunner.com/2018/12/why-you-should-be-using-pathlib"
weight:
links:
  - "til/programming/python/python-reliable-path.md"
---

> Since Python 3.4


`pathlib` is object oriented. It is more elegant than `os.path`. For example, if we need the parent folders of the currrent file, we need `os.path.dirname()`,

```python
import os

print(f"file: {__file__}")
# file: main.py

# Using os.path
os__file_absolute_path = os.path.abspath(__file__)
print(f"Using os.path:: file absolute path: {os__file_absolute_path}")
# Using os.path:: file absolute path: /home/runner/pathlib/main.py

os__file_in_folder = os.path.dirname(os__file_absolute_path)
print(f"Using os.path:: file is in folder: {os__file_in_folder}")
# Using os.path:: file is in folder: /home/runner/pathlib
```

It is much more easier to get the folder using `pathlib`.

```python
from pathlib import Path

print(f"file: {__file__}")
# file: main.py

# Using pathlib
path__file = Path(__file__)
print(f"Using pathlib:: path__file: {path__file}; using .resolve method: {path__file.resolve()}")
# Using pathlib:: path__file: main.py; using .resolve method: /home/runner/pathlib/main.py

path__file_in_folder = path__file.resolve().parent
print(f"Using pathlib:: path__file_in_folder: {path__file_in_folder}")
# Using pathlib:: path__file_in_folder: /home/runner/pathlib
```


`pathlib` also [supports](https://docs.python.org/3/library/pathlib.html#basic-use) [glob](https://docs.python.org/3/library/glob.html).

The full code is [avaible on repl.it](https://replit.com/@emptymalei/pathlib-is-better-than-ospath-in-python).