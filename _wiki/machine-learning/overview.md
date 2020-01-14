---
title: "Machine Learning"
excerpt: "machine learning"
date: 2018-05-25
toc: true
category:
- 'Machine Learning::Basics'
tag:
- 'Statistical Learning'
- 'Machine Learning'
- 'Basics'
weight: 0
---


## What is Machine Learning

There are many objectives of machine learning. Two of the most applied objectives are classifications and regressions. In classifications and regression, the following four factors are relevant.

1. A dataset $\tilde{\mathscr D}(\tilde{\mathbf X}, \tilde{\mathbf y})$ with $\tilde{\mathbf X}$ being the features and $\tilde{\mathbf y}$ being the values to be predicted;
2. A set of encoders $\mathscr T_i$ that maps the features $\tilde{\mathbf X}$ into new features $\mathbf X$ and predicting values $\tilde{\mathbf y}$ into new values $\mathbf y$. The dimensions of $\tilde{\mathbf X}$ and $\mathbf X$ may not be the same. Or simply $\mathscr T(\tilde{\mathscr D}) \to \mathscr D$
3. A model $f(\mathbf X;\mathbf \theta)\to \bar{\mathbf y}$ that maps $\mathbf X$ to the values with $\mathbf x$ being a set of input features. $f$ may also be a set of functions.
4. A test method $\mathscr C(\mathbf y, \bar{\mathbf y})$ that indicates how well the model is performing.

The dataset $\tilde{\mathscr D}$ is first encoded by $\mathscr T$, $\mathscr D(\mathbf X, \mathbf y) = \mathscr T(\tilde{\mathscr D})$. The dataset is feeded into the model, $\bar{\mathbf y} = f(\mathbf X;\mathbf \theta)$. The model is then tested with the test method, $\mathscr C$. By requiring the test method to satisfy some specific conditions, we solve the model parameters $\mathbf\theta$.


## References

1. [Mehta, P., Bukov, M., Wang, C. H., Day, A. G. R., Richardson, C., Fisher, C. K., & Schwab, D. J. (2019). A high-bias, low-variance introduction to Machine Learning for physicists. Physics Reports, 810, 1–124.](https://doi.org/10.1016/j.physrep.2019.03.001)