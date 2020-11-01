---
layout: til
title: "IPython or Jupyter Notebook Magics"
date: 2015-12-04
author: Lei Ma
comments: true
category:
- programming
tags:
- Python
- Jupyter
excerpt: IPython or Jupyter Notebook Magics
---

Summary of the [video lectures on IPython](https://www.udemy.com/get-started-with-the-ipython-notebook/learn/#/lecture/1077138):

* `%` is line level magic, which only affects the code starting from the position of it, while `%%` is cell level magic;
* List all the magics: `%lsmagic`;
* Timing of a cell: `%timeit `, for example, `%timeit np.cos(1.3)`;
* Write the content of the cell to a file by using `%%writefile output.py`;
* Bash commands can be used in the command mod, by simply using a `!`, for example, `!ls -l` (Tab to autocomplete);
* `%run output.py` can run the file;
* Run a background job using `%%python --bg --out output.txt` then followed by the python code;
* Plots inline can be made using `%matplotlib inline`;
