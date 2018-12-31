---
layout: til
title: "Python If on Numbers"
date: 2018-12-31
author: OctoMiao
category:
- programming
- basics
tag:
- Python
excerpt: If on int is dangerous
---

A bug that is so easy to miss.

```python
my_data = {'score': 5 }
restult = int(my_data.get('score')) if my_data.get('score') else None
```
Naively, I would think this will deal with it correctly even with a missing key.

However, if `'score'` ever becomes 0, this will fail since `my_data.get('score')` returns 0 and 0 is calculated as false in this case. Then the results goes to None which is not what we want.

```python
my_data = {'score': 0 }
restult = int(my_data.get('score')) if my_data.get('score') else None
# result is actually None, but we might require it to be 0
```
