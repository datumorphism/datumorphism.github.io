---
title: "Time Series Forecasting with Deep Learning"
description: "Evaluate time series models"
date: 2022-04-24
categories:
  - "Time Series"
tags:
  - "Machine Learning"
  - "Time Series"
  - "Deep Learning"
references:
- name: "Lim B, Zohren S. Time Series Forecasting With Deep Learning: A Survey. arXiv [stat.ML]. 2020. Available: http://arxiv.org/abs/2004.13408"
  link: "http://arxiv.org/abs/2004.13408"
  key: "Lim2020"
weight: 2
---


## The Encoder-Decoder Framework

Many of the models for {{< c "wiki/forecasting/forecasting-problem.md" "time series forecasting" >}} using deep learning are following some sort of encoder-decoder architecture.

1. Encoder: $g_{\text{enc}}(x^{(i)} _ {t-K:t}, u^{(i)} _ {t-K:t}) \to z_t$,
2. Decoder: $g_{\text{dec}}(z_t, u^{(i)} _ {t+1: t+H}) \to y_{t+1:t+H}$.



[^Lim2020]: {{< cite key="Lim2020" >}}
