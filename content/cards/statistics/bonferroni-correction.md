---
title: "Bonferroni Correction"
date: "2020-04-01"
description: "Bonferroni correction is very useful in a multiple comparison problem"
categories:
  - "Statistics"
tags:
  - "Statistics"
  - "Hypothesis Testing"
references:
  - name: "Contributors to Wikimedia projects. Bonferroni correction. In: Wikipedia [Internet]. 22 Feb 2022 [cited 18 Apr 2022]. Available: https://en.wikipedia.org/wiki/Bonferroni_correction"
    link: https://en.wikipedia.org/wiki/Bonferroni_correction
  - name: "Contributors to Wikimedia projects. Multiple comparisons problem. In: Wikipedia [Internet]. 11 Apr 2022 [cited 18 Apr 2022]. Available: https://en.wikipedia.org/wiki/Multiple_comparisons_problem"
    link: "https://en.wikipedia.org/wiki/Multiple_comparisons_problem"
---


In a single hypothesis testing problem, we the {{< c "wiki/statistical-hypothesis-testing/type-1-error-and-type-2-error.md" "type I error" >}}: Rejecting the one null hypothesis when it is actually true. Given a threshold $\alpha$, we can find out the interval $\Gamma$ that leads to a probability of rejecting the hypothesis $p\leq\alpha$ (single-sided).

In a {{< c "cards/statistics/multiple-comparison-problem.md" "multiple comparisons problem" >}}, type I error is ambiguous. Suppose we have $m$ hypotheses $H_1, \cdots, H_i, H_m$. If we define the type I error as committing at least one type I error, this is the **FamilyWise Error Rate** (**FWER**).

In such a problem, we look for intervals $\Gamma^\alpha_i$ that lead to $p_i\leq \alpha/m$, where $m$ is the number of hypotheses. These intervals will together make sure our jointed type I error greater than $\alpha$.

