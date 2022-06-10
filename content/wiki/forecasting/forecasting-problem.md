---
title: "The Time Series Forecasting Problem"
description: "Forecasting time series"
date: "2022-04-24"
categories:
  - "Time Series"
tags:
  - "Machine Learning"
  - "Time Series"
  - "Deep Learning"
references:
  - name: "Lim B, Zohren S. Time Series Forecasting With Deep Learning: A Survey. arXiv [stat.ML]. 2020. Available: http://arxiv.org/abs/2004.13408"
    link: "http://arxiv.org/abs/2004.13408"
  - name: "Hewamalage H, Ackermann K, Bergmeir C. Forecast Evaluation for Data Scientists: Common Pitfalls and Best Practices. arXiv [cs.LG]. 2022. Available: http://arxiv.org/abs/2203.10716"
    link: "http://arxiv.org/abs/2203.10716"
    key: "Hewamalage2022"
weight: 1
---

## Forecasting Problem

A time series forecasting problem can be formulated as the following.

Given a dataset $\mathcal D$, with

1. $y^{(i)}_t$, the sequential variable to be forecasted,
2. $x^{(i)}_t$, exogenous data for the time series data,
3. $u^{(i)}_t$, some features that can be obtained or planned in advance,

where ${}^{(i)}$ indicates the $i$th variable, ${}_ t$ denotes time. In a forecasting task, we use $y^{(i)} _ {t-K:t}$, $x^{(i) _ {t-K:t}}$, and $u^{(i)} _ {t-K:t+H}$, to forecast the future $y^{(i)} _ {t+1:t+H}$.


{{< figure src="../assets/forecasting-problem/time-series-forecasting-problem.jpg" >}}

A model $f$ will use $x^{(i)} _ {t-K:t}$ and $u^{(i)} _ {t-K:t+H}$ to forecast $y^{(i)} _ {t+1:t+H}$.


## The Time Delay Embedding Representation

The time delay embedding representation of a time series forecasting problem is a concise representation of the forecasting problem [^Hewamalage2022].

For simplicity, we only write down the representation for a problem with time series $y_{1}, \cdots, y_{t}$, and forecasting $y_{t+1}$. We rewrite the series into a matrix, in an autoregressive way,

{{< m >}}
\begin{align}
\mathbf Y = \begin{bmatrix}
y_1 & y_2 & \cdots & y_p &\Big| & {\color{red}y_{p+1}} \\
y_{1+1} & y_{1+2} & \cdots & y_{1+p} &\Big| &  {\color{red}y_{1+p+1}} \\
\vdots & \vdots & \ddots & \vdots &\Big| &  {\color{red}\vdots} \\
y_{i-p+1} & y_{i-p+2} & \cdots & y_{i} &\Big| &  {\color{red}y_{i+1}} \\
\vdots & \vdots & \ddots & \vdots &\Big| &  {\color{red}\vdots} \\
y_{t-p+1} & y_{t-p+2} & \cdots & y_{t} &\Big| &  {\color{red}y_{t+1}} \\
\end{bmatrix}
\end{align}
{{< /m >}}

which indicates that we will use everything on the left, a matrix of shape $(t-p+1,p)$, to predict the vector on the right (in red).


[^Hewamalage2022]: {{< cite key="Hewamalage2022" >}}