---
layout: til
title: "Python Long String"
date: 2018-12-31
author: Lei Ma
category:
- programming
- basics
tags:
- Python
summary: Python long string formatting
---


```
QUERY = (
    'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
    'WHERE state = "TX" '
    'LIMIT 100')
```

is equivalent to

```
QUERY='SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` WHERE state = "TX" LIMIT 100'
```