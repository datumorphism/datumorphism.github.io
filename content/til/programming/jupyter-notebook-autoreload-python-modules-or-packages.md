---
layout: til
title: "Auto-reload Python Packages or Python Modules in Jupyter Notebook"
date: 2019-05-12
author: Lei Ma
comments: true
category:
- programming
tags:
- Python
- Jupyter
excerpt: Python package or python module autoreloading in jupyter notebook
---

In many cases, we include local packages or modules in jupyter notebooks. While it makes the code easier to read, packages or modules have to be hot reloaded everytime we make some changes to them.


```
%load_ext autoreload
%autoreload 2
```

More about this jupyter notebook magic can be found in the [documentation](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html).