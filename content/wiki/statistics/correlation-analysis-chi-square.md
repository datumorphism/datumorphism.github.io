---
title: "Chi-square Correlation Test for Nominal Data"
excerpt: "Detecting correlations using Pearson's chi square correlation test"
date: 2018-11-18
toc: true
category:
- 'Statistics'
tag:
- 'Statistics'
- 'Basics'
- 'Correlation'
references:
- name: "Data Mining by Jiawei Han, Micheline Kamber, Jian Pei"
  title: ''
weight: 3
---


In this article, we will discuss the chi-square correlation test for detecting correlations between two series.

## Steps

1. Find out all the possible values of the two nominal series A and B;
2. Count the co-occurrences of the combinations (A, B);
3. Calculate the expected co-occurrences of the combinations (A, B);
4. Calculate chi-square;
5. Determine whether the hypothesis can be rejected.

## Define the Series

Suppose we are analyzing two series A and B. Series A can take values $a_1$ and $a_2$, while series B can take values $b_1$ , $b_2$ and $b_3$.

$$
\begin{align}
A &:= \{a1, a2\} \\
B &:= \{b1,b2,b3\}
\end{align}
$$

As an example, we will use the following A and B series for our calculations in this article.

| index | A | B |
|--|---|---|
| 1 | a1 | b2 |
| 2 | a1 | b2 |
| 3 | a1 | b1 |
| 4 | a2 | b1 |
| 5 | a2 | b3 |
| 6 | a2 | b2 |
| 7 | a1 | b2 |
| 8 | a2 | b2 |


## Count Co-ocurrences

To analyze correlations between the two series, we need to look at whether the values of series A and those of series B would occur together. For example, we would like to know the possibility of values for B if we have $a_1$ occurred.

<div class="notes--info" markdown="1">
One of the extreme examples is that A and B are exactly the same. In this case, we would know that the value for B is always the same as A for each row. Then we would know that all the possible combinations of (A, B) are
1. (a1, a1)
2. (a2, a2)

We could construct the occurrence table.

|   |  a1 | a2 |
|--|---|---|
| a1 |  number of occurrences | 0 |
| a2 |  0 | number of occurrences |

</div>

Now we construct a contigency table to denote the ocurrences of the values,  (A, B).

|  | a1 | a2 |
|--|---|---|
| b1 | 1 | 1 |
| b2 | 3 | 2 |
| b3 | 0 | 1 |

where the cells are filled with the number of occurrences of the corresponding combinations. For example, the combination (a1, b1) occurred once, thus 1 in the first row first column.

This table records the **observed frequencies**, which we denote as table O and each cell is denoted as $o_{ij}$.

<div class="notes--info" markdown="1">
This table tells us about the possible correlations already. Imagine we have two columns that are exactly the same, we would have a table that have large number of occurences on the diagonal elements.
</div>

<div class="notes--warning" markdown="1">
However, those numbers in the table depends on the number of rows that we have in our original table. To find the actual correlation, we need to normalize it. We could simply divided everything by the total number of rows in the original table. But Pearson had a better idea.
</div>

Pearson's chi-square correlation is a smart idea.

First of all, we define an expectation table E. Each element of E is calculated as

$$
e_{ij} = \frac{ \text{number of } a_i * \text{ number of } b_j }{ \text{ total number of rows in original table } }
$$

<div class="notes--info" markdown="1">
This $e_{ij}$ serves as the average occurance of each combinations of $a_i$ and $b_j$. If we have $a_i$ in each row but only one $b_j$ occurrences, the average is 1. This mean that given $b_j$ we would definitely only see one $a_i$.

When we have multiple $a_i$ and $b_j$, this average still works. Suppose we have $a_1$ occurred 4 times in total and we have a total of 8 rows. Assuming that this $a_1$ will appear randomly in the rows, what is the average probability to see this $a_1$ if we choose a random row? It is $4/8=0.5$. Then we will expect $1\times 0.5=0.5$ occurrences $a_1$ for one occurance of $b_2$. If we have 3 occurances of $b_2$, we would expect to see $3\times 0.5==1.5$ occurrences of $a_1$.

This is why it is treated as expected frequencies of each combinations.

As a side note, suppose we have A and B exactly the same, and they all have the same values, a1.

| index | A | B |
|--|---|---|
| 1 | a1 | b1 |
| 2 | a1 | b1 |
| 3 | a1 | b1 |
| 4 | a1 | b1 |
| 5 | a1 | b1 |
| 6 | a1 | b1 |
| 7 | a1 | b1 |
| 8 | a1 | b1 |

Then we expect $e_{11} = n$, where $n=8$ is the number of rows.
</div>

Now if we compare the original table with this one,

$$
o_{ij} - e_{ij}
$$

we get the deviation from the expected table. With a few little twitches, we would define

$$
\chi^2 = \sum_{i,j} \frac{ (o_{ij} - e_{ij})^2 } { e_{ij} }
$$

<div class="notes--info" markdown="1">
If A and B are the same and each possible values occurred m times, then we would have

$$
o_{ij} = e_{ij} = \delta_{ij} * m.
$$

Then we get
$$
\chi^2 = 0
$$

Then we say this chi-square analysis doesn't reject our hypothesis that these two columns are correlated.
</div>

## How to Use the Number Chi-square

The final question is how to use the result. We usually have a threshold $\chi_0^2$. Whenever our calculated value is larger than this one, we decide that our analysis reject the hypothesis that the two columns are correlated.
This value $\chi_0^2$ can be found in the textbooks.

## Other Methods

1. [Kendall rank correlation coefficient](https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient)
2. [Spearman's rank correlation coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient)
