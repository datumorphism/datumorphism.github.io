---
title: Model Selection
date: 2020-11-08
categories:
  - Model Selection
tags:
  - Model Selection
  - AIC
  - BIC
  - MDL
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
weight: 1
---


Suppose we have a generating process that generates some numbers based on a distribution. Based on a data sample, we could reconstruct some sort of theoretical models to represent the actual generating process.


{{< figure src="../assets/model-selection/model-selection-good-or-bad-1.png" title="Which is a Good Model?  (1)" caption="The black curve represent the generating process. The red rectangle is a very simple model that captures some major samples. The blue step-wise model is capturing more sample data but with more parameters." >}}

In the above example, the red model on the left is not that good in most cases while the blue model seems to be better. In reality, the choice depends on the usage of the model. But we can already tell that the balance is between how well the model describes the data and how complicated the model is.

To make it even more conflicting, the following illustration shows another generating process and two corresponding models.

{{< figure src="../assets/model-selection/model-selection-good-or-bad-2.png" title="Which is a Good Model? (2)" caption="The black curve represent the generating process. The red rectangle is a very simple model that captures some major samples. The blue step-wise model is capturing more sample data but with more parameters." >}}

In this case, we might agree that the red simple model is probably good enough for many situations. While the blue model is captures more features of the data, we have to deal with more parameters.

## What is a Good Model?

Presumably, a good model should be

- plausibility (we do not like models that explain suicide rates primarily based on the coverage of Internet Explorer),
- balance of parsimony and goodness-of-fit (we can not use models that perform badly but a good-performing model with ten-thousand parameters is not exactly a good one either most of the time),
- coherence of the underlying assumptions,
	- easy to understand when it breaks down,
- consistency with known results,
	- especially with the simple and basic phenomena,
- ability to explain rather than describe data,
- extent to which model predictions can be falsified through experiments.


{{< message class="info" title="Parsimony">}}
The parsimony concept is a natural consequence of Occam's razor: We choose the simple model for more explanatory power.

For example, [the instance theory](http://intelligence.leima.is/bio-intelligence/cognition/instance-theory/) by Logan is a good model to explain the [lexical decision task](http://intelligence.leima.is/bio-intelligence/cognition/lexical-descion-task). It is not a perfect model, but it bears parsimony.
{{< /message >}}


## How to choose a model?


To choose a good model, we need a framework to compare two models. The comparison shall at least address the goodness-of-fit and parsimony.


Many methods have been proposed to deal with the balance between [parsimony](/wiki/model-selection/parsimony-of-models) and [goodness-of-fit](/wiki/model-selection/goodness-of-fit), e.g.,

- Information criteria (IC) such as {{< c "cards/statistics/aic.md" "AIC" >}} and {{< c "cards/statistics/bic.md" "BIC" >}},
- Minimum description length ({{< c "cards/statistics/mdl.md" "MDL" >}}),
- Bayes factors.


Here we demonstrate how IC can tell us which model is better. We calculate the IC of all the models at hand and specify the delta

{{< m >}}
\Delta _i = \mathrm{IC}_i - \operatorname{min} \mathrm{IC}.
{{< /m >}}

Then we specify the weights of models

{{< m >}}
w_i = \frac{ \exp\{-\Delta_i/2\} }{ \sum_{m=1}^M \exp\{-\Delta_m/2\} }.
{{< /m >}}

The model with larger weight $w_i$ is a better model.

{{< message title="Akaike weight and Schwarz weight" class="info" >}}

If we use AIC as the IC in the formula, this weight $w_i$ is called Akaike weight; If we use BIC, the weight $w_i$ is called Schwarz weight.

{{< /message >}}

There are other criteria too. For example, we can use the [minimum description length](/cards/statistics/mdl)or the [Bayes factors](/cards/statistics/bayes-factors).
