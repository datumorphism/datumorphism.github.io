---
title: "Cross Validation"
date: 2021-05-06
categories:
- 'Machine Learning::Theories'
tags:
- 'Learning Theory'
- 'Cross Validation'
references:
  - name: "Murphy, K. P. (2012). Probabilistic Machine Learning: An Introduction."
    link: "https://mitpress.mit.edu/books/machine-learning-1"
    key: "Murphy2012"
links:
  - cards/machine-learning/learning-theories/learning-problem.md
published: true
---


Cross validation is a method to estimate the {{< c "cards/machine-learning/learning-theories/learning-problem.md" "risk" >}}.

To perform cross validation, we split the train dataset $\mathcal D$ into $k$ folds, with each fold denoted as $\mathcal D_k$.

Given a model $\mathcal M(x, \theta)$ with parameter $\theta$, there are two steps in the modelling procedure:
- Fitting
  - where the estimator estimates the parameters $\hat \theta$;
  - The fitting step can be denoted as $\hat\theta = \mathcal F(\mathcal D, \mathcal M)$
- Prediction
  - where the estimated parameters are fed into the model to get the predictions $\mathcal M(\hat\theta)$;
  - The prediction step can be denoted as $\hat y = \mathcal M (x, \hat\theta)$.

For a $k$th fold, we perform fitting on the datasets $\mathcal D_{\sim k}$ where ${}_{\sim k}$ means all datasets that are not the $k$th fold, the perform prediction using the $k$th dataset $\mathcal D_k$. The risk can be estimated as

{{< m >}}
\begin{align}
R_k =& \frac{1}{\lvert D_k \rvert}\sum_{i\in \mathcal D_k} L (y_i, \hat y ) \\
=&  \frac{1}{\lvert D_k \rvert}\sum_{i\in \mathcal D_k} L (y_i,\mathcal M (x_i, \hat\theta_{\sim k}) ) \\
=& \frac{1}{\lvert D_k \rvert} \sum_{i\in \mathcal D_k} L (y_i,\mathcal M (x_i, \mathcal F(\mathcal D_{\sim k}, \mathcal M) ) ).
\end{align}
{{< /m >}}

The overall $K$-fold cross validation risk $R$ is the sum of all the risks $R_k$,

{{< m >}}
\begin{align}
R = \sum_{k=1}^K R_k
\end{align}
{{< /m >}}


If we have $\lvert \mathcal D_k \rvert = K$, we will have only one sample in the prediction step. This is called leave one out cross validation, aka LOOCV.
