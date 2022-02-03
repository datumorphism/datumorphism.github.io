---
layout: til
title: "Binning Data Values using Pandas"
description: "Convert continuous values into bins in pandas"
date: 2021-03-10
authors:
  - "LM"
categories:
  - programming
  - basics
tags:
  - Python
  - Pandas
  - numpy
references:
  - name: "pandas.cut"
    link: "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.cut.html"
weight:
links:
  - ""
---

Use the `pd.cut` function. The bins argument is using `(]` are the segments. The official documentation comes with detailed examples.



If pandas is not an option, one could use [`numpy.digitize`](https://numpy.org/doc/stable/reference/generated/numpy.digitize.html) to find which bin the elements belong to.
