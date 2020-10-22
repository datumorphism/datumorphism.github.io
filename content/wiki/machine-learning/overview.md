---
title: "Machine Learning Overview"
excerpt: "machine learning"
date: 2018-05-25
toc: true
category:
- 'Machine Learning::Basics'
tag:
- 'Statistical Learning'
- 'Machine Learning'
- 'Basics'
weight: 1
references:
  - name: "Mehta, P., Bukov, M., Wang, C. H., Day, A. G. R., Richardson, C., Fisher, C. K., & Schwab, D. J. (2019). A high-bias, low-variance introduction to Machine Learning for physicists. Physics Reports, 810, 1–124."
    link: "https://doi.org/10.1016/j.physrep.2019.03.001"
  - name: "Shalev-Shwartz, S., & Ben-David, S. (2013). Understanding machine learning: From theory to algorithms. Understanding Machine Learning: From Theory to Algorithms"
    link: "https://doi.org/10.1017/CBO9781107298019"
---


## What is Machine Learning

There are many objectives of machine learning. Two of the most applied objectives are classifications and regressions. In classifications and regression, the following four factors are relevant.

<figure markdown="1">
![](../assets/overview/machine-learning-framework.png)
<figcaption markdown="1">
A simple framework of machine learning. The dataset $\tilde{\mathscr D}$ is first encoded by $\mathscr T$, $\mathscr D(\mathbf X, \mathbf Y) = \mathscr T(\tilde{\mathscr D})$. The dataset is feeded into the model, $\bar{\mathbf Y} = f(\mathbf X;\mathbf \theta)$. The model is then tested with the test method, $L_{f, \mathscr D}(h)$. By requiring the test method to satisfy some specific conditions, we solve the model parameters $\mathbf\theta$.
</figcaption>
</figure>

1. Input:
   0. Domain knowledge $\tilde{\mathscr K_D}$.
      1. on features,
      2. on target values,
      3. on relation between features and target values.
   1. A dataset $\tilde{\mathscr D}(\tilde{\mathbf X}, \tilde{\mathbf Y})$ with $\tilde{\mathbf X}$ being the features and $\tilde{\mathbf Y}$ being the values to be predicted;
      1. features (domain set): $\tilde{\mathbf X}$,
      2. target values (label set): $\tilde{\mathbf Y}$.
      3. relations between features and target values: $f(\mathbf X) \to \mathbf Y$.
2. A set of "encoders" $\mathscr T_i$ that maps the features $\tilde{\mathbf X}$ into machine readable new features $\mathbf X$ and predicting values $\tilde{\mathbf y}$ into machine readable new values $\mathbf y$. The dimensions of $\tilde{\mathbf X}$ and $\mathbf X$ may not be the same. In summary, $\mathscr T(\tilde{\mathscr D}) \to \mathscr D$.
3. A model (aka, prediction rule, predictor, hypothesis) $h(\mathbf X;\mathbf \theta)\to \bar{\mathbf Y}$ that maps $\mathbf X$ to the values with $\mathbf X$ being a set of input features. $h$ may also be a set of functions.
4. A measurement of the model performance, $L_{f, \mathscr D}(h)$.
   1. Error of model: $L_{f, \mathscr D}(h) = \mathscr L(h(\mathbf X), f(\mathbf X))$, where $\mathscr L$ is distance operator.


