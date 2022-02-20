---
title: "Autoregressive Model"
description: "Time series modeling"
date: 2018-06-20T15:58:49-04:00
categories:
- 'Time Series Data'
tags:
- 'ARMA'
weight: 2
---

## Autoregressive

Given a time series $\{T^i\}$, a simple predictive model can be constructed using an autoregressive model.

$$
\begin{equation}
T^t = \sum_{i=1}^p \beta_i T^{t - i} + \beta^t + \beta^0.
\end{equation}
$$

Such a model is usually called an AR(p) model due to the fact that we are using data back in $p$ steps.

{{< card title="Differential Equation" >}}

For simplicity we will look at a AR(1) model. Assume the time series has a step size of $dt$, our model can be rewritten as

$$
T^t = \beta_1 T^{t - 1} + \beta^t + \beta^0
$$

which can be rewritten in the following way

$$
(1 - \beta_1) T^t = \beta_1 T^{t - 1} - \beta_1 T^t + \beta^t + \beta^0.
$$

We can cast it into a differential equation form

$$
T(t) = - dt \frac{\beta_1}{1 - \beta_1} T'(t) + \frac{\beta^t + \beta^0}{1 - \beta_1}.
$$

For AR(2), we have

$$
T^t = \beta_1 T^{t - 1} + \beta_2 T^{t - 2} + \beta^t + \beta^0
$$

casted as


\begin{align*}
&(1-\beta_1 - \beta_2) T^t = -\beta_1 (T^t - T^{t - 1}) - \beta_2 (T^t - T^{t-1} + T^{t-1} - T^{t - 2}) + \beta^t + \beta^0 \\\\
\Rightarrow &(1-\beta_1 - \beta_2) T^t = -dt \beta_1 (T^t - T^{t - 1})/dt - 2dt\beta_2 (T^t - T^{t-1} + T^{t-1} - T^{t - 2})/(2dt) + \beta^t + \beta^0 \\\\
\Rightarrow &T^t = - dt \frac{\beta_1 + 2\beta_2}{1-\beta_1 - \beta_2} T'(t) + \frac{\beta^t + \beta^0}{1-\beta_1 - \beta_2}
\end{align*}


We could also write this into a combination of first order derivative and second order derivative form but I think it is better to be only first order derivative.

{{</card>}}