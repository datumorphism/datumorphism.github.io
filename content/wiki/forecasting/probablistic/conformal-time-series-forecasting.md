---
title: "Conformal Time Series Forecasting"
date: "2022-04-19"
categories:
  - "Time Series"
tags:
  - "Machine Learning"
  - "Time Series"
  - "Conformal Prediction"
  - "Probabilistic"
references:
  - name: "Stankevičiūtė K, Alaa AM, Van Der Schaar M. Conformal Time-Series Forecasting. [cited 9 Feb 2022]. Available: https://proceedings.neurips.cc/paper/2021/hash/312f1ba2a72318edaaa995a67835fad5-Abstract.html"
    link: "[Vapnik, V. N. (2000). The Nature of Statistical Learning Theory. Springer New York. ](https://proceedings.neurips.cc/paper/2021/hash/312f1ba2a72318edaaa995a67835fad5-Abstract.html)"
    key: "Stankevičiūtė2022"
---

Conformal time series forecasting is a probabilistic forecasting method using {{< c "wiki/statistical-estimation/conformal-prediction.md" >}}.

For any given model $\mathcal M$, conformal time series forecasting trains on a training dataset $\mathcal D_{\text{Train}}$ then calculates a {{< c "wiki/statistical-estimation/confidence-interval.md" >}} using a calibration dataset $\mathcal D_{\text{Calibration}}$. The confidence interval is directly used for inference. This framework is called the inductive conformal prediction (ICP).

{{< e "cards/machine-learning/learning-theories/induction-deduction-transduction.md" >}}

## How to Forecast the Confidence Interval

For a dataset $\mathcal D$, we split it, e.g., $\mathcal D_{\text{Training}}$ and $\mathcal D_{\text{Calibration}}$, where

{{< m >}}
\begin{align}
\lvert \mathcal D_{\text{Training}} \rvert  &= n \\
\lvert \mathcal D_{\text{Calibration}} \rvert  &= m.
\end{align}
{{< /m >}}

After training the model, we use the calibration dataset $\mathcal D_{\text{Calibration}}$ to find the distribution of a predefined nonconformity measure, e.g.,

{{< m >}}
R_i = \Delta( \mathcal M(x^{(i)}\vert \mathcal D_{\text{Training}}) , y^{(i)} ).
{{< /m >}}


By looking at the distribution, we find the interval that leads to $P(R_i > R_{th}) \sim 0.05$. In practice, we can simply use quantiles. Using the $R_{th}$, we can find the corresponding deviation of predictions, $\epsilon$.

For inference, we simply use $[\hat y - \epsilon, \hat y + \epsilon]$ as our predicted range.


## Multihorizon Forecasting

In a multihorizon forecasting problem, we need to correct our ranges using the  {{< c "cards/statistics/bonferroni-correction.md" >}}.