---
title: Model Comparison
tags:
  - AIC
  - BIC
references:
  - link: https://www.coursera.org/lecture/linear-regression-model/collinearity-and-parsimony-ukePA
    name: Collinearity and Parsimony from Linear Regression and Modeling on Coursear
  - link: https://www.oxfordhandbooks.com/view/10.1093/oxfordhb/9780199957996.001.0001/oxfordhb-9780199957996-e-14
    name: Vandekerckhove, J., & Matzke, D. (2015). Model comparison and the principle of parsimony. Oxford Library of Psychology.
links:
  - wiki/model-selection/measures-of-generalizability.md
  - wiki/model-selection/goodness-of-fit.md
  - cards/statistics/bayes-factors.md
  - cards/statistics/aic.md
  - cards/statistics/bic.md
  - cards/statistics/fia.md
  - cards/statistics/mdl.md
---

The parsimony model comes from the idea of Occam's razor: We choose the simple model that has more explanatory power.

[The instance theory](http://intelligence.leima.is/bio-intelligence/cognition/instance-theory/) is a good model to explain the [lexical decision task](http://intelligence.leima.is/bio-intelligence/cognition/lexical-descion-task) but it is not the only one. However, it simply makes it popular.


## What is a Good Model?

A good model should be presumably

- plausibility
- balance of parsimony and goodness-of-fit
- coherence of the underlying assumptions
	- easy to understand when it breaks down
- consistency with known results
	- especially with the simple and basic phenomena
- ability to explain rather than describe data
- extent to which model predictions can be falsified through experiments.


## How to choose a model?


It takes some thinking and calculations to choose a model.

- Model comparison (Logan does a great job in his paper about [Instance Theory of Attention and Memory](http://intelligence.leima.is/bio-intelligence/cognition/instance-theory/))
- Model selection
- Hypothesis testing

## Compare Models

Many methods deals with the balance between [parsimony](/wiki/model-selection/parsimony-of-models) and [goodness-of-fit](/wiki/model-selection/goodness-of-fit)

- Information criteria: AIC and BIC
- Minumum description length
- Bayes factors

### Information Criteria: IC

We calculate the IC of all the models at hand, and specify the delta

$$
\Delta _i = \mathrm{IC}_i - \operatorname{min} \mathrm{IC}
$$

calculate the weights of models

$$
w_i = \frac{ \exp{-\Delta_i/2} }{ \sum_{m=1}^M \exp{-\Delta_m/2} }
$$

We prefer the model with larger weight $w_i$.

If we use AIC for IC in the formula, this weight $w_i$ is called Akaike weight; If we use BIC, the weight $w_i$ is called Schwarz weight.

### MDL

Fisher Information Approximation is one of the methods to determine the [minimum description length](/cards/statistics/mdl).


### Bayes Factors

[Bayes factors](/cards/statistics/bayes-factors)
