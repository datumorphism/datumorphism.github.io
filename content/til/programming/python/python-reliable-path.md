---
layout: til
title: "Python Reliable Path to File"
date: 2018-12-31
author: Lei Ma
categories:
- programming
- basics
tags:
- Python
summary: Find the actual path to file
references:
- name: "How to reliably open a file in the same directory as a Python script @ StackOverflow"
  link: https://stackoverflow.com/a/4060259
- name: "Miscellaneous operating system interfaces @ The Python Standard Library"
  link: https://docs.python.org/3.7/library/os.html
- name: "os.path — Common pathname manipulations"
  link: https://docs.python.org/3.7/library/os.path.html
---

## Using `pathlib`

```python
from pathlib import Path

__location__ = Path(__file__).parent.resolve()
```

As an example, we could read a file `my_file.json` located at the same folder as the python script.

```python
with open(os.path.join(__location__, 'my_file.json'), 'r') as f:
    data_from_file = json.loads( f.read() )
```

### Playground

{{< repl url="https://repl.it/@emptymalei/python-reliable-path?lite=true" >}}






## Using `os`

Python `os` module provides several useful functions too. This is **NOT** recommended anymore. But if one insists, we can easily make it work.


The following code will determine the path to the file.

```python
__location__ = os.path.realpath(
  os.path.join(
    os.getcwd(),
    os.path.dirname(os.path.abspath(__file__))
  )
)
```

For the same example as above, we could read a file `my_file.json` located at the same folder as the python script.

```python
with open(os.path.join(__location__, 'my_file.json'), 'r') as f:
    data_from_file = json.loads( f.read() )
```

We can understand how it works by breaking it down.

1. `os.getcwd()`: get current working directory. Current working directory is defined as where the python script is executed.

    ```terminal
    ➜  Downloads python temp.py
    os.getcwd:  /Users/datumorphism/Downloads
    ➜  ~ python Downloads/temp.py
    os.getcwd:  /Users/datumorphism
    ```
2. `__file__`: is basically the file name. Suppose we have a python script with name `main.py`.

   ```python
   print('__file__: ', __file__)
   ```

   will return `__file__:  main.py`.

3. `os.path.abspath` retrieves the absolute path of the file.

   ```python
   file_absolute_path = os.path.abspath(__file__)
   ```

4. `os.path.join` joins the strings into path, intelligently.

   ```python
   print('os.path.join("datumorphism", "main.py"): ', os.path.join("datumorphism", "main.py") )
   ```

   will return `os.path.join("datumorphism", "main.py"):  datumorphism/main.py`.



### Playground

{{< repl url="https://repl.it/@emptymalei/Reliable-Path-to-File?lite=true" >}}

