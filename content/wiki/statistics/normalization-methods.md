---
title: "Normalization Methods for Numeric Data"
description: "Detecting correlations using correlations for numerical data"
date: 2018-11-18
category:
- 'Statistics'
tags:
- 'Statistics'
- 'Basics'
- 'Normalization'
references:
- name: "Data Mining by Jiawei Han, Micheline Kamber, Jian Pei"
  title: ''
weight: 5
---


Normalization of data is critical for statistical analysis and feature engineering.

## Min-max Normalization

This method is linear and straightforward.

Suppose we are analyzing series A, with elements $a_i$. We already know the min and max of the series, $a_{min}$ and $a_{max}$.

Now we would like to normalize the series to be within the range $[a_{min}', a_{max}']$. We simply solve the value of $a' _ i$ in
$$
\frac{(a'_i - a_{min}')}{ ( a'_{max} - a'_{min}  ) } = \frac{(a_i - a_{min})}{ ( a_{max} - a_{min}  ) },
$$
where everything on the right hand side is known and $a_{min}'$ and $a_{max}'$ are chosen as the new min and max to be scaled to.

{{< message class="warning" >}}
The problem with this method is that the min and max has to be known, which is not always the case.

Another problem is that outliers would have a big effect on this method. Such examples could be the prices of houses. There might be one house in the database that has an extremely low price such as 1 euro, or extermely high price such as one billion euros.
{{</message>}}

## Z-score Normalization

Z-score normalization method normalizes the data using the standard deviation since standard deviation measures how are the data points devivate from the mean.

$$
a'_i = \frac{ (a_i - \bar A) }{ \sigma_A }
$$

{{< message class="info">}}
For a series with only one value, $a'_i = 0$. For series of the form $ (a, -a, a, -a) $ where $a> 0$,

$$
\sigma_A = a.
$$

Then we have the normalized series to be
$$
( 1, -1, 1, -1 )
$$
{{< /message >}}

## Decimal Scaling

Basically shifting the data with some powers of 10.

$$
a'_i = a_i/ 10^j
$$

choose $j$ so that the new values are not larger than 1.
