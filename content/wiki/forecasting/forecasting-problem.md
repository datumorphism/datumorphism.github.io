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
  - name: "Januschowski T, Gasthaus J, Wang Y, Salinas D, Flunkert V, Bohlke-Schneider M, et al. Criteria for classifying forecasting methods. Int J Forecast. 2020;36: 167–177. doi:10.1016/j.ijforecast.2019.05.008"
    link: "https://www.sciencedirect.com/science/article/pii/S0169207019301529"
    key: "Januschowski2019"
weight: 1
---

There are many different types of tasks on time series data:

- classification,
- anomaly detection,
- forecasting.



## Forecasting Problem

A time series forecasting problem can be formulated as the following.

Given a dataset $\mathcal D$, with

1. $y^{(i)}_t$, the sequential variable to be forecasted,
2. $x^{(i)}_t$, exogenous data for the time series data,
3. $u^{(i)}_t$, some features that can be obtained or planned in advance,

where ${}^{(i)}$ indicates the $i$th variable, ${}_ t$ denotes time. In a forecasting task, we use $y^{(i)} _ {t-K:t}$, $x^{(i) _ {t-K:t}}$, and $u^{(i)} _ {t-K:t+H}$, to forecast the future $y^{(i)} _ {t+1:t+H}$.


{{< figure src="../assets/forecasting-problem/time-series-forecasting-problem.jpg" >}}

A model $f$ will use $x^{(i)} _ {t-K:t}$ and $u^{(i)} _ {t-K:t+H}$ to forecast $y^{(i)} _ {t+1:t+H}$.

The above formulation is mostly focusing on the point forecasts. Alternative, the {{< c "cards/forecasting/prediction-space.md" "probabilistic view" >}} of a forecasting problem has been a very hot topic in recent years.


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


## Methods of Forecasting Methods

T. Januschowsk et al proposed a framework to classify the different forecasting methods.[^Januschowski2019]


{{< mermaid >}}
flowchart TB


subgraph Objective


params_shared["Parameter Shared Accross Series"]


params_shared --"True"-->Global
params_shared --"False"-->Local

uncertainty["Uncertainty in Forecasts"]
uncertainty --"True"--> Probabilistic["Probabilistic Forecasts:\n forecasts with predictive uncertainty"]
uncertainty --"False"--> Point["Point Forecasts"]

computational_complexity["Computational Complexity"]





end



subgraph Subjective


structural_assumptions["Strong Structural Assumption"] --"Yes"--> model_driven["Model-Driven"]
structural_assumptions --"No"--> data_driven["Data-Driven"]

model_comb["Model Combinations"]

discriminative_generative["Discriminative or Generative"]

theoretical_guarantees["Theoretical Guarantees"]

predictability_interpretability["Predictability and Interpretibility"]

end
{{< /mermaid >}}




[^Hewamalage2022]: {{< cite key="Hewamalage2022" >}}
[^Januschowski2019]: {{< cite key="Januschowski2019" >}}
