---
layout: til
title: "Calculated Columns in Pandas"
date: 2018-05-20
modified: 2018-05-20
author: Lei Ma
category:
- programming
- basics
tag:
- Python
- Pandas
excerpt: Create new columns in pandas
---

Pandas has got two very useful functions called `groupby` and `transform`. In this TIL, I will demonstrate how to create new columns from existing columns.

First of all, I create a new data frame here.

```python
df = pd.DataFrame( {'city':['London','London','Berlin','Berlin'], 'rent': [1000, 1400, 800, 1000]} )
```

which looks like

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>rent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>London</td>
      <td>1000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>London</td>
      <td>1400</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Berlin</td>
      <td>800</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Berlin</td>
      <td>1000</td>
    </tr>
  </tbody>
</table>
</div>


I will create a new column called total, which will host the total rents of the corresponding cities.

```python
df['total'] = df.groupby('city').transform('sum')
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>rent</th>
      <th>total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>London</td>
      <td>1000</td>
      <td>2400</td>
    </tr>
    <tr>
      <th>1</th>
      <td>London</td>
      <td>1400</td>
      <td>2400</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Berlin</td>
      <td>800</td>
      <td>1800</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Berlin</td>
      <td>1000</td>
      <td>1800</td>
    </tr>
  </tbody>
</table>
</div>


Next, I will create a new column called percent which will contain the percentage

```python
df['percent'] = df['rent']/df['total']
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>rent</th>
      <th>total</th>
      <th>percent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>London</td>
      <td>1000</td>
      <td>2400</td>
      <td>0.416667</td>
    </tr>
    <tr>
      <th>1</th>
      <td>London</td>
      <td>1400</td>
      <td>2400</td>
      <td>0.583333</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Berlin</td>
      <td>800</td>
      <td>1800</td>
      <td>0.444444</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Berlin</td>
      <td>1000</td>
      <td>1800</td>
      <td>0.555556</td>
    </tr>
  </tbody>
</table>
</div>
