---
title: "Learning Rate"
description: "Find a good learning rate"
date: "2021-11-01"
authors:
  - "L Ma"
categories:
  - "Neural Networks"
tags:
  - "Machine Learning"
  - "Deep Learning"
  - "Basics"
  - "Learning Rate"
references:
  - name: "Pointer I. Programming PyTorch for deep learning: Creating and deploying deep learning applications. Sebastopol, CA: O’Reilly Media; 2019."
    link: "https://www.oreilly.com/library/view/programming-pytorch-for/9781492045342/"
    key: "Pointer2019"
  - name: "Howard J, Thomas R. Hyperparam schedule. In: fastai [Internet]. [cited 30 Nov 2021]. Available: https://docs.fast.ai/callback.schedule.html#Learner.lr_find"
    link: "https://docs.fast.ai/callback.schedule.html#Learner.lr_find"
    key: "fastaidocs"
  - name: "Howard J, Gugger S. Deep Learning for Coders with Fastai and PyTorch: AI Applications Without a PhD. O’Reilly Media, Incorporated; 2020. Available: https://www.oreilly.com/library/view/deep-learning-for/9781492045519/"
    link: "https://www.oreilly.com/library/view/deep-learning-for/9781492045519/"
    key: "Howard&Gugger2020"
links:
  - "wiki/machine-learning/neural-networks/artificial-neural-networks.md"
  - "cards/machine-learning/neural-networks/neural-networks-initialization.md"
---

Finding a suitable learning rate for our model training is crucial.

A safe but time wasting option is to use search on a grid of parameters. However, there are smarter moves.

{{< message title="Karpathy's Constant" class="info" markdownify="n" >}}

An empirical learning rate $3^{-4}$ for Adms, aka, Karpathy's constant, was started as a tweet by Andrei Karpathy.

{{< tweet user="karpathy" id="801621764144971776" >}}

{{< tweet user="karpathy" id="801694597009113088" >}}

{{< /message >}}


## Smarter Method

A smarter method is to start with small learning rate and increase it on each mini-batch, then observe the loss vs learning rate (mini-batch in this case). The learning rate that leads to the greatest gradient decline is a suitable learning rate [^Pointer2019] [^Howard&Gugger2020] [^fastaidocs].


{{< figure src="../assets/learning-rate/learning_rate_fastai.png" caption="Figure taken from [fastai docs](https://docs.fast.ai)" >}}

The code for this method can be found on the [GitHub repo of fastai](https://github.com/fastai/fastai/blob/351f4b9314e2ea23684fb2e19235ee5c5ef8cbfd/fastai/callback/schedule.py#L284).

[^Pointer2019]: {{< cite key="Pointer2019" >}}
[^Howard&Gugger2020]: {{< cite key="Howard&Gugger2020" >}}
[^fastaidocs]: {{< cite key="fastaidocs" >}}