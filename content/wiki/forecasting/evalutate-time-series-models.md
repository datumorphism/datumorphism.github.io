---
title: "Evaluating Time Series Models"
description: "Evaluate time series models"
date: 2022-04-08
categories:
  - "Time Series"
tags:
  - "Machine Learning"
  - "Time Series"
references:
- name: "Cerqueira V, Torgo L, Mozetic I. Evaluating time series forecasting models: An empirical study on performance estimation methods. arXiv [cs.LG]. 2019. Available: http://arxiv.org/abs/1905.11744"
  link: "http://arxiv.org/abs/1905.11744"
weight: 3
---

Evaluating time series models is usually different from most other machine learning tasks as we usually don't have i.i.d. data.

## Out-of-sample

{{< figure src="../assets/evaluate-time-series-models/oos-sliding-window.png" caption="Out-of-Sample with Sliding Window" >}}

If the sliding window size is 1, then we have the simplest out-of-sample holdout scenario.


## Prequential



{{< figure src="../assets/evaluate-time-series-models/block-gap.png" caption="Prequential with Gap" >}}

{{< figure src="../assets/evaluate-time-series-models/block-grow.png" caption="Prequential with Growing Train" >}}

{{< figure src="../assets/evaluate-time-series-models/block-slide.png" caption="Prequential with Sliding Blocks" >}}



## Cross-validation



{{< figure src="../assets/evaluate-time-series-models/cv.png" caption="Cross-validation" >}}

{{< figure src="../assets/evaluate-time-series-models/cv-removed.png" caption="Cross-validation with Neighbor removed" >}}