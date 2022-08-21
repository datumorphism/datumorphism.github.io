---
title: "Empirical Correlation Coefficient (CORR)"
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

The Empirical Correlation Coefficient (**CORR**) is an evaluation metric in time series forecasting,[^Lai2017]

{{< m >}}
\mathrm{CORR} = \frac{1}{N} \sum_{i=1}^N \frac{
  \sum_t (y^{(i)}_t - \bar y^{(i)} ) ( \hat y^{(i)}_t -\bar{ \hat y}^{(i)}  )
}{
  \sqrt{
    \sum_t (y^{(i)}_t - \bar y^{(i)} )^2 ( \hat y^{(i)}_t -\bar{\hat y}^{(i)}  )^2
  }
}
{{< /m >}}


where $y^{(i)}$ is the $i$th time series, ${} _ t$ denotes the time step $t$, and $\bar y^{(i)}$ is the mean of the $i$th forecasted series, i.e., $\bar y^{(i)} = \operatorname{mean}( y^{(i)} _ { t \in \\{T _ f, T _ {f+1}, \cdots T _ {f+H}\\} } )$.


[^Lai2017]: {{< cite key="Lai2017" >}}
