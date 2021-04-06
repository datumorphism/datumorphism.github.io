---
title: "Deal with Rare Categories Using Pandas"
description: "Deal with rare categories using pandas"
date: 2021-03-10
authors:
  - "LM"
categories:
  - "data"
tags:
  - "feature"
  - "feature engineering"
  - "pandas"
references:
  - name: "pandas.DataFrame.mask"
    link: "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mask.html"
weight:
links:
  - "til/programming/pandas/pandas-new-column-from-other.md"
  - "wiki/machine-learning/feature-engineering/missing-data.md"
---


We will illustrate how to deal with rare categories using pandas mask.


```python
import pandas as pd

#############
# Create fake names
frequent_names = list('ABC')
rare_names = list('DEF')

dataset = sum(
    [[i]*10 for i in frequent_names] + [[i]*2 for i in rare_names],
    []
)

# Create a series based on the names
series = pd.Series(dataset)

print(series)

# Find the counts of the names in the series
series_counts = series.value_counts()
print(series_counts)


# Find names that has less than 10 counts
# And create a mask
mask = series.isin(series_counts.loc[series_counts<10].index)
print(mask)


# Set these rare names to X
series[mask] = 'X'

# Check the new series
print(series.value_counts())
```


The original series has value counts

```
C    10
A    10
B    10
F     2
D     2
E     2
```

The new series has value counts

```
C    10
A    10
B    10
X     6
```