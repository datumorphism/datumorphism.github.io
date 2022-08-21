---
title: "Root Relative Squared Error (RSE)"
description: ""
date: 2022-08-21T20:43:36+02:00
authors:
  - "Lei Ma"
categories:
  - "Time Series"
tags:
  - "Time Series"
  - "Forecasting"
references:
  - name: "Lai G, Chang W-C, Yang Y, Liu H. Modeling Long- and Short-Term Temporal Patterns with Deep Neural Networks. arXiv [cs.LG]. 2017. Available: http://arxiv.org/abs/1703.07015"
    link: "http://arxiv.org/abs/1703.07015"
    key: "Lai2017"
garden:
  - "seedling"
---

The Root Relative Squared Error (**RSE**) is an evaluation metric in time series forecasting,[^Lai2017]

{{< m >}}
\mathrm{RSE} = \frac{
  \sqrt{ \sum_{i, t} ( y^{(i)}_t - \hat y^{(i)}_t )^2 }
}{
  \sqrt{ \sum_{i, t} ( y^{(i)}_t - \bar y )^2 }
}
{{< /m >}}


where $y^{(i)}$ is the $i$th time series, ${} _ t$ denotes the time step $t$, and $\bar y$ is the mean of the forecasted series, i.e., $\bar y = \operatorname{mean}(y^{(i\in\\{0, 1, \cdots, N\\})} _ { t\in \\{T _ f, T _ {f+1}, \cdots T _ {f+H}\\} })$.


[^Lai2017]: {{< cite key="Lai2017" >}}
