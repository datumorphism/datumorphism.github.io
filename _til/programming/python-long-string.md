---
layout: til
title: "Python Long String"
date: 2018-12-31
author: OctoMiao
category:
- programming
- basics
tag:
- Python
excerpt: Python long string formatting
---


```
QUERY = (
    'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
    'WHERE state = "TX" '
    'LIMIT 100')
```

is evquivalent to

```
QUERY='SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` WHERE state = "TX" LIMIT 100'
```