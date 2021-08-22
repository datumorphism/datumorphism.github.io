---
title: "Generative Model: Variational Auto-Encoder"
date: 2021-08-13
category:
  - "Machine Learning"
tags:
  - "Self-supervised Learning"
  - "Generative Model"
  - "VAE"
  - "Basics"
references:
  - name: "Liu X, Zhang F, Hou Z, Wang Z, Mian L, Zhang J, et al. Self-supervised Learning: Generative or Contrastive. arXiv [cs.LG]. 2020. Available: http://arxiv.org/abs/2006.08218"
    link: "http://arxiv.org/abs/2006.08218"
  - name: "Doersch C. Tutorial on Variational Autoencoders. arXiv [stat.ML]. 2016. Available: http://arxiv.org/abs/1606.05908"
    link: "http://arxiv.org/abs/1606.05908"
    key: "Doersch2016"
weight: 4
links:
  - "wiki/machine-learning/generative-models/autoencoder.md"
  - "wiki/machine-learning/bayesian/elbo.md"
  - "wiki/machine-learning/bayesian/latent-variable-models.md"
  - "cards/statistics/reparametrization-expectation-sampling.md"
---

Variational Auto-Encoder (VAE) is very different from {{< c "wiki/machine-learning/generative-models/autoencoder.md" >}}. In VAE, we introduce a variational distribution $q$ to help us work out the weighted integral after introducing the latent space variable $z$,

{{< m >}}
\begin{align}
\ln p_\theta(x) &= \ln \int p_\theta (x\mid z) p(z) \,\mathrm d z \\
&= \ln \int \frac{q_{\phi}(z\mid x)}{q_{\phi}(z\mid x)} p_\theta (x\mid z) p(z) \, \mathrm d z\\
& \geq - \left[ D_{\mathrm{KL}} ( q_{\phi}(z\mid x) \mathrel{\Vert} p(z)  )  -  \mathbb E_q ( \ln p_\theta (x\mid z) ) \right] \\
&\equiv - F(x).
\end{align}
{{< /m >}}

$F(x)$ is the free energy, while the negative of it, $-F(x)$, is the so-called {{< c "wiki/machine-learning/bayesian/elbo.md" "Evidence Lower Bound (ELBO)" >}}.

In the above derivation,

- ${}_\theta$ is the model for inference, and
- ${}_\phi$ is the model for variational approximation.

{{< figure src="../assets/generative-variational-autoencoder/simple-vae.png" caption="Structure of VAE" >}}

Doersch wrote a very nice tutorial on VAE[^Doersch2016]. We can find the detailed structures of VAE.

Another key component of VAE is the {{< c "cards/statistics/reparametrization-expectation-sampling.md" "reparametrization trick" >}}. The variational approximation $q_\phi$ is usually a Gaussian distribution. Once we get the parameters for the Gaussian distribution, we will have to sample from the Gaussian distribution based on the parameters. However, this sampling process prohibits us from propagating errors. The {{< c "cards/statistics/reparametrization-expectation-sampling.md" "reparametrization trick" >}} solves this problem.


## Loss Explanation

{{< figure src="../assets/generative-variational-autoencoder/vae-loss-explained.png" caption="VAE Loss Explained [Doersch2016]" >}}



[^Doersch2016]: {{< cite "Doersch2016" >}}
