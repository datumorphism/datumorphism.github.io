---
title: "Kendall Tau Correlation"
date: 2019-07-20
categories:
- 'Statistics'
tags:
- 'Statistics'
- 'Correlation'
references:
- name: Kendall, M. G. (1938). A new measure of correlation. Biometrika, 30(1–2), 81–93.
  link: https://academic.oup.com/biomet/article-abstract/30/1-2/81/176907?redirectedFrom=fulltext
- name: Kendall rank correlation coefficient
  link: https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient
- name: Rank correlation
  link: https://en.wikipedia.org/wiki/Rank_correlation
---

## Definition

* two series of data: $X$ and $Y$
* cooccurance of them: $(x_i, x_j)$, and we assume that $i<j$
* concordant: $x_i < x_j$ and $y_i < y_j$; $x_i > x_j$ and $y_i > y_j$; denoted as $C$
* discordant: $x_i < x_j$ and $y_i > y_j$; $x_i > x_j$ and $y_i < y_j$; denoted as $D$
* neither concordant nor discordant: whenever equal sign happens

Kendall's tau is defined as

$$
\begin{equation}
\tau = \frac{C- D}{\text{all possible pairs of comparison}} = \frac{C- D}{n^2/2 - n/2}
\end{equation}
$$