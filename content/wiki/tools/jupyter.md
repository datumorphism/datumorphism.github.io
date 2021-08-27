---
title: "Jupyter Notebook"
description: "Jupyter Notebook is a useful tool for data scientists"
date: 2018-06-20T15:58:49-04:00
toc: true
categories:
- Tools
tags:
- Tools
- Jupyter
references:
- name: "Built-in magic command @ ipython"
  link: https://ipython.readthedocs.io/en/stable/interactive/magics.html
links:
  - "wiki/programming-languages/python/_index.md"
weight: 1
---


## Magics

1. `%lsmagic` will show all the magics, including line magics and cell magics.

   1. Line magics are magics start with one `%`;
   2. Cell magics are magics that can be used in the whole cell even with line breaks, where the cell should start with `%%`.

2. `%env` can be used when setting environment variables inside the notebook.
   ```
   %env MONGO_URI=localhost:27072
   ```

3. `%%bash` is a cell magic that allows bash commands in the cell.

   ```
   %%bash
   ls
   pip install datahubxyz
   ```

4. `%%time` enables timing of functions.
   ```
   %%time
   for i in range(1000):
       i*i
   ```

   `%timeit` is the corresponding line magic which times the function of the corresponding line.

## Documentation

1. `?functionname` (`IPython`, `Jupyter`): doc string of the function with better formatting
2. `dir(modulename)` (`Python`, `IPython`, `Jupyter`): to get the list of attributes of the module.
3. `modulename.functionname.__doc__` (`Python`, `IPython`, `Jupyter`): to get the doc string of the function.