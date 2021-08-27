---
title: "SRM: Structural Risk Minimization"
date: 2021-02-18
categories:
- 'Machine Learning::Theories'
tags:
- 'Data'
- 'Loss'
references:
  - name: "Structural risk minimization @ Wikipedia"
    link: "https://en.wikipedia.org/wiki/Structural_risk_minimization"
  - name: "Murphy, K. P. (2012). Probabilistic Machine Learning: An Introduction."
    link: "https://mitpress.mit.edu/books/machine-learning-1"
links:
  - cards/machine-learning/learning-theories/learning-problem.md
  - cards/machine-learning/learning-theories/empirical-risk-minimization.md
published: true
---

{{< c "cards/machine-learning/learning-theories/empirical-risk-minimization.md" "ERM" >}} may lead to overfitting since ERM only selects the model to fit the train data well.

Though [Regularized Risk](/cards/machine-learning/learning-theories/empirical-risk-minimization) is designed to attack the overfitting problem based on the empirical risk and the complexity of the model, the hyperparamter to determine the weight of the two composition is not easy to decide systematically.

There are two main categories of structural risk minimization method:
- Cross-validation (CV),
- Using Statistical Learning Theory (SLT).
