---
title: "Neyman-Pearson Theory"
excerpt: "Neyman-Pearson theory is a framework of hypothesis testing"
date: 2022-04-02
toc: true
categories:
  - "Statistics Hypothesis Testing"
tags:
  - "Statistics"
  - "Basics"
  - "Hypothesis Testing"
references:
  - name: "Shafer G, Vovk V. A tutorial on conformal prediction. arXiv [cs.LG]. 2007. Available: http://arxiv.org/abs/0706.3188"
    link: "http://arxiv.org/abs/0706.3188"
    key: "Shafer2007"
  - name: "Perezgonzalez JD. Fisher, Neyman-Pearson or NHST? A tutorial for teaching data testing. Front Psychol. 2015;6: 223. doi:10.3389/fpsyg.2015.00223"
    link: "https://www.frontiersin.org/articles/10.3389/fpsyg.2015.00223/full"
    key: "Perezgonzalez2015"
  - name: "26.1 - Neyman-Pearson Lemma. In: PennState: Statistics Online Courses [Internet]. [cited 2 Apr 2022]. Available: https://online.stat.psu.edu/stat415/lesson/26/26.1"
    link: "https://online.stat.psu.edu/stat415/lesson/26/26.1"
    key: "pennstate_stats"
  - name: "Contributors to Wikimedia projects. Likelihood-ratio test. In: Wikipedia [Internet]. 10 Jun 2021 [cited 2 Apr 2022]. Available: https://en.wikipedia.org/wiki/Likelihood-ratio_test"
    link: "https://en.wikipedia.org/wiki/Likelihood-ratio_test"
    key: "wiki_likelihood-ratio_test"
garden:
  - "seedling"
weight: 4
---

The Neyman-Pearson hypothesis testing tests two hypothesis, hypothesis $H$, and an alternative hypothesis $H_A$.

## Neyman-Pearson Lemma

The Neyman-Pearson Lemma is an very intuitive lemma to understand how to choose a hypothesis. The [lecture notes from PennState](https://online.stat.psu.edu/stat415/lesson/26/26.1) is a very good read on this topic[^pennstate_stats].


## An example


For simplicity, we assume that there exists a test statistic $T$ and $T$ can be used to measure how likely the hypothesis $H$ is true, e.g., the hypothesis $H$ is false, corresponds to $T$ being small.

{{< message class="warning" >}}

The reference from Shafer2007 assumes a random variable $T$ to be large if the hypothesis $H$ is false[^Shafer2007].

{{< /message >}}

One example is the ratio of likelihood[^wiki_likelihood-ratio_test],


{{< m >}}
T \to L(H)/L(H_A),
{{< /m >}}

where $T$ will be large if $H$ is true.


To be able to judge the hypothesis, we "loosely" define a probability

{{< m >}}
p_H = P(T\leq c\vert H),
{{< /m >}}

where $c$ is a preset critical value of $T$. Given a threshold $\epsilon$ for $p_H$, we claim the hypothesis $H$ can be rejected if $p_H<\epsilon$.





[^Shafer2007]: {{< cite key="Shafer2007" >}}
[^Perezgonzalez2015]: {{< cite key="Perezgonzalez2015" >}}
[^pennstate_stats]: {{< cite key="pennstate_stats" >}}
[^wiki_likelihood-ratio_test]: {{< cite key="wiki_likelihood-ratio_test" >}}