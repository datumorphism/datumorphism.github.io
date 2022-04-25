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

