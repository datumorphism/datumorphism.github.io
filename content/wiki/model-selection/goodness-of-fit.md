---
title: Goodness-of-fit
date: 2020-11-08
categories:
  - Model Selection
tags:
  - Model Selection
references:
  - link: "https://www.oxfordhandbooks.com/view/10.1093/oxfordhb/9780199957996.001.0001/oxfordhb-9780199957996-e-14"
    name: "Vandekerckhove, J., & Matzke, D. (2015). Model comparison and the principle of parsimony. Oxford Library of Psychology."
links:
  - wiki/model-selection/model-selection.md
  - wiki/model-selection/parsimony-of-models.md
  - wiki/model-selection/measures-of-generalizability.md
  - cards/statistics/likelihood.md
weight: 2
---


Does the data agree with the model?
- Calculate the distance between data and model predictions.
- Apply Bayesian methods such as likelihood estimation: likelihood of observing the data if we assume the model; the results will be a set of fitting parameters.
- ...


Why don't we always use goodness-of-fit as a measure of [the goodness of a model](/wiki/model-selection/model-selection)?

- We may experience overfitting.
- The model may not be intuitive.

This is why we would like to balance it with [parsimony](/wiki/model-selection/parsimony-of-models) using some [measures of generalizability](/wiki/model-selection/measures-of-generalizability).


{{< message class="info" title="K-means and overfitting" >}}
The overfitting problem is easily demonstrated using the K-means model.

Suppose we use $k=1$, i.e., considering only the data point and no neighbors, we will get a model that is 100% agreeing with the data. If we require only goodness of fit, we may as well choose this $k=1$ model. However, such a model is useless since it is the dataset itself without any other insights.

{{< /message >}}