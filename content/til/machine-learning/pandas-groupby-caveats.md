---
title: "Pandas Groupby Does Not Guarantee Unique Content in Groupby Columns"
date: 2020-04-20
authors:
  - Lei Ma
categories:
- machine-learning
tags:
- Python
- Pandas
summary: Pandas Groupby Does Not Guarantee Unique Content in Groupby Columns, it also considers the datatypes. Dealing with mixed types requires additional attentioin.
---


Pandas groupby also considers the data types.

```python
import pandas as pd

data = [{"student": 1, "score": 1}, {"student": "1", "score": 2}]

df = pd.DataFrame(data)

df.groupby("student").count()
```

What we see is

```
        score
student
1       1
1       1
```

The value `1` and `"1"` are different.

Suppose we are given a bunch of scores of students and we would like to use the median of scores as the final scores. Somehow, the student ids are encoded either in strings or in integers. It is crucial to make sure the data types are the same before grouping.
