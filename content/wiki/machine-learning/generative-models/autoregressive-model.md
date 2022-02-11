---
title: "Generative Model: Autoregressive Model"
date: 2021-08-13
categories:
  - "Machine Learning"
tags:
  - "Self-supervised Learning"
  - "Generative Model"
  - "Autoregressive Model"
  - "Basics"
references:
  - name: "Uria B, Côté M-A, Gregor K, Murray I, Larochelle H. Neural Autoregressive Distribution Estimation. arXiv [cs.LG]. 2016. Available: http://arxiv.org/abs/1605.02226"
    link: "http://arxiv.org/abs/1605.02226"
    key: "Uria2016"
  - name: "Triebe O, Laptev N, Rajagopal R. AR-Net: A simple Auto-Regressive Neural Network for time-series. arXiv [cs.LG]. 2019. Available: http://arxiv.org/abs/1911.12436"
    link: "http://arxiv.org/abs/1911.12436"
    key: "Triebe2019"
  - name: "Ho G. George Ho. In: Eigenfoo [Internet]. 9 Mar 2019 [cited 19 Sep 2021]. Available: https://www.eigenfoo.xyz/deep-autoregressive-models/"
    link: "https://www.eigenfoo.xyz/deep-autoregressive-models"
    key: "Ho2019"
  - name: "Papamakarios G, Pavlakou T, Murray I. Masked Autoregressive Flow for Density Estimation. arXiv [stat.ML]. 2017. Available: http://arxiv.org/abs/1705.07057"
    link: "http://arxiv.org/abs/1705.07057"
    key: "Papamakarios2017"
  - name: "Germain M, Gregor K, Murray I, Larochelle H. MADE: Masked autoencoder for distribution estimation. 32nd International Conference on Machine Learning, ICML 2015. 2015;2: 881–889. Available: http://arxiv.org/abs/1502.03509"
    link: "http://arxiv.org/abs/1502.03509"
    key: "Germain2015"
  - name: "Liu X, Zhang F, Hou Z, Wang Z, Mian L, Zhang J, et al. Self-supervised Learning: Generative or Contrastive. arXiv [cs.LG]. 2020. Available: http://arxiv.org/abs/2006.08218"
    link: "http://arxiv.org/abs/2006.08218"
    key: "Liu2020"
  - name: "Lippe P. Tutorial 12: Autoregressive Image Modeling — UvA DL Notebooks v1.1 documentation. In: UvA Deep Learning Tutorials [Internet]. [cited 20 Sep 2021]. Available: https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial12/Autoregressive_Image_Modeling.html"
    link: "https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial12/Autoregressive_Image_Modeling.html"
    key: "Lippe"
  - name: "rogen-george. rogen-george/Deep-Autoregressive-Model. In: GitHub [Internet]. [cited 20 Sep 2021]. Available: https://github.com/rogen-george/Deep-Autoregressive-Model"
    link: "https://github.com/rogen-george/Deep-Autoregressive-Model"
    key: "rogen"
weight: 2
links:
  - "wiki/machine-learning/neural-networks/deep-autoregressive-networks.md"
  - "wiki/time-series/autoregressive-model.md"
---


An autoregressive (AR) model is autoregressive,

$$
\begin{equation}
\log p_\theta (x) = \sum_{t=1}^T \log p_\theta ( x_{t} \mid \{x_{<t}\} ).
\end{equation}
$$



{{< figure src="../assets/generative-autoregressive-model/generative-ar-basics-1.jpg" >}}

In the above example, the likelihood is modeled as

{{< m >}}
\begin{align}
p_\theta (x) &= \Pi_{t=1}^T p_\theta (x_t \mid x_{1:t-1}) \\
&= p_\theta(x_2 \mid x_{1:1}) p_\theta(x_3 \mid x_{1:2}) \cdots p_\theta(x_T \mid x_{1:T-1})
\end{align}
{{< /m >}}

Taking the log of it

{{< m >}}
\ln p_\theta (x) = \sum_{t=1}^T \ln p_\theta (x_t \mid x_{1:t-1})
{{< /m >}}




{{< message title="Notations and Conventions" >}}

In AR models, we have to mention the preceding nodes ($\{x_{<t}\}$) of a specific node ($x_{t}$). For $t=5$, the relations between $\{x_{<5}\}$ and $x_5$ is shown in the following illustration.

![](assets/autoregressive/ar-notations.jpg)

There are different notations for such relations.

- In Uria et al., the authors use $p(x_{o_d}\mid \mathbf x_{o_{<d}})$ [^Uria2016].
- In Liu et al. and Papamakarios et al., the authors use $p(x_{t}\mid \mathbf x_{1:t-1})$ [^Liu2020][^Papamakarios2017].
- In Germain et al., the authors use $p(x_t\mid \mathbf x_{<t})$ [^Germain2015].

In the current review, we expanded the vector notation $\mathbf x_{<t}$ into a set notation as it is not necessarily a vector.


{{< /message >}}







[^Uria2016]: {{< cite key="Uria2016" >}}

[^Triebe2019]: {{< cite key="Triebe2019" >}}

[^Ho2019]: {{< cite key="Ho2019" >}}

[^Papamakarios2017]: {{< cite key="Papamakarios2017" >}}

[^Germain2015]: {{< cite key="Germain2015" >}}

[^Liu2020]: {{< cite key="Liu2020" >}}

[^Lippe]: {{< cite key="Lippe" >}}


[^rogen]: {{< cite key="rogen" >}}


