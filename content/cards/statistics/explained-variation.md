---
title: "Explained Variation"
description: ""
date: 2021-05-05T18:05:47+02:00
authors:
  - "Lei Ma"
categories:
  - "statistics"
tags:
  - "analysis of variance"
references:
  - name: "Explained variation"
    link: "https://en.m.wikipedia.org/wiki/Explained_variation"
weight:
links:
  - "cards/information/fraser-information.md"
---





Using {{< c "cards/information/fraser-information.md" "Fraser information" >}}, we can define a relative information gain by a model

$$
\rho_C ^2 = 1 - \frac{  \exp( - 2 F(\theta_1) ) }{  \exp( - 2 F(\theta_0) ) },
$$

where $F(\theta_0)$ is the Fraser information assuming the features and target variables are all independent variables while $F(\theta_1)$ is the Fraser information of a model that predicts the target variable using the features.

$\rho_C^2$ is also the explained variation as it indicates the dispersion in the data that is explained using the features.