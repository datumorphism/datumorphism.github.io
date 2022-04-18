---
title: "Multiple Comparison Problem"
date: "2020-04-01"
categories:
  - "Statistics"
tags:
  - "Statistics"
  - "Hypothesis Testing"
references:
  - name: "Contributors to Wikimedia projects. Multiple comparisons problem. In: Wikipedia [Internet]. 11 Apr 2022 [cited 18 Apr 2022]. Available: https://en.wikipedia.org/wiki/Multiple_comparisons_problem"
    link: "https://en.wikipedia.org/wiki/Multiple_comparisons_problem"
  - name: "Zeni G, Fontana M, Vantini S. Conformal Prediction: a Unified Review of Theory and New Challenges. arXiv [cs.LG]. 2020. Available: http://arxiv.org/abs/2005.07972"
    link: "http://arxiv.org/abs/2005.07972"
    key: "Zeni2020"
garden:
  - "seedling"
---

In a multiple comparisons problem, we deal with multiple statistical tests simultaneously.

## Examples

We see such problems a lot in IT companies. Suppose we have a website and would like to test if a new design of a button can lead to some changes in five different KPIs (e.g., view-to-click rate, click-to-book rate, ...).

In multi-horizon time series forecasting, we sometimes choose to forecast multiple future data points in one shot. To properly find the confidence intervals of our predictions, one approach is the so called conformal prediction method. This becomes a multiple comparisons problem because we have to tell if we can reject at least one true null hypothesis. In a paper by Zeni et al[^Zeni2020], the confidence interval has to be adjusted due to a specific definition of type I error for the family of hypotheses {{< c "cards/statistics/bonferroni-correction.md" "FWER" >}}.

[^Zeni2020]: {{< cite key="Zeni2020" >}}