---
title: "Feasibility of Learning"
date: 2021-10-17
categories:
  - "Learning Theory"
tags:
  - "Learning Theory"
  - "Basics"
references:
  - name: "Abu-Mostafa, Yaser S and Magdon-Ismail, Malik and Lin, Hsuan-Tien. Learning from Data. AMLBook; 2012. Available: https://www.semanticscholar.org/paper/Learning-From-Data-Abu-Mostafa-Magdon-Ismail/1c0ed9ed3201ef381cc392fc3ca91cae6ecfc698"
    link: "https://www.semanticscholar.org/paper/Learning-From-Data-Abu-Mostafa-Magdon-Ismail/1c0ed9ed3201ef381cc392fc3ca91cae6ecfc698"
    key: "Abu-Mostafa2012"
  - name: "Bernstein J. Machine learning is just statistics + quantifier reversal. In: jeremybernste [Internet]. [cited 1 Nov 2021]. Available: https://jeremybernste.in/writing/ml-is-just-statistics"
    link: "https://jeremybernste.in/writing/ml-is-just-statistics"
    key: "Bernstein2021"
  - name: "Guedj B. A Primer on PAC-Bayesian Learning. arXiv [stat.ML]. 2019. Available: http://arxiv.org/abs/1901.05353"
    link: "http://arxiv.org/abs/1901.05353"
    key: "Guedj2019"
  - name: "Zhang C, Bengio S, Hardt M, Recht B, Vinyals O. Understanding deep learning requires rethinking generalization. arXiv [cs.LG]. 2016. Available: http://arxiv.org/abs/1611.03530"
    link: "http://arxiv.org/abs/1611.03530"
    key: "Zhang2016"
links:
  - "wiki/machine-learning/overview.md"
weight: 1
published: true
---

Why is learning from data even possible? To discuss this problem, we need a framework for learning. Operationally, we can think of learning as the following framework[^Abu-Mostafa2012].

{{< figure src="../assets/feasibility-of-learning/abu-mostafa-learning-framework.png" caption="Abu-Mostafa2012" >}}


## Naive View

Naively speaking, a model should have two key properties,

1. enough capacity to hold the necessary information embedded in the data, and
2. a method to find the combination of parameters so that the model can generate/complete new data.

Most neural networks have enough capacity to hold the necessary information in the data[^Zhang2016]. The problem is, the capacity is so large. Why does backprop even work? How did backprop find a suitable set of parameters that can generalize?





[^Abu-Mostafa2012]: {{< cite key="Abu-Mostafa2012" >}}
[^Zhang2016]: {{< cite key="Zhang2016" >}}