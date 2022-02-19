---
title: "KL Divergence"
description: "Kullback–Leibler divergence indicates the differences between two distributions"
date: 2021-04-05
authors:
  - "LM"
categories:
  - "statistics"
tags:
  - "probability"
  - "distance"
references:
  - name: "Kullback–Leibler divergence @ Wikipedia"
    link: "https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence"
  - key: "Kurt2017"
    name: "Kullback-Leibler Divergence Explained @ COUNT BAYESIE by Will Kurt"
    link: "https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained"

weight:
links:
  - "wiki/machine-learning/bayesian/latent-variable-models.md"
---


Given two distributions $p(x)$ and $q(x)$, the Kullback-Leibler divergence is defined as

{{< m >}}
D_\text{KL}(p(x) \parallel q(x) ) = \int_{-\infty}^\infty p(x) \log\left(\frac{p(x)}{q(x)}\right)\, dx = \mathbb E_{p(x)} \left[\log\left(\frac{p(x)}{q(x)}\right) \right].
{{< /m >}}

{{< message class="info" title="Connection to Entropy" >}}

Notice that this expression is quite similar to entropy,

$$
H(p(x)) = \int_{-\infty}^{\infty} p(x) \log p(x) \, dx.
$$

The entropy describes the lower bound of the number of bits (if we use $\log_2$) of how the information can be compressed. By looking at the expression of the KL divergence, we intuitively interpret it as the information loss if we use distribution $q(x)$ to approximate distribution $p(x)$, [Kurt2017](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained)

$$
D_\text{KL}(p(x) \parallel q(x) ) = \mathbb E_{p(x)} \left[\log p(x)- \log q(x)\right] .
$$


{{</message>}}

Kullback-Leibler divergence is also called relative entropy. In fact, KL divergence can be decomposed into cross entropy $H(p) = -\int_{-\infty}^\infty p(x) \log q(x)\, dx$ and entropy $H(p) = -\int_{-\infty}^\infty p(x) \log p(x)\, dx$

{{< m >}}
D_\text{KL}(p \parallel q) = \int_{-\infty}^\infty  p(x) \log p(x)\, dx - \int_{-\infty}^\infty p(x) \log  q(x) \, dx = - H(p) + H(p, q),
{{< /m >}}

which is

{{< m >}}
D_\text{KL}(p \parallel q) + H(p) = H(p, q).
{{< /m >}}

## What does it mean?

We assume two uniform distributions,

{{< m >}}
p(x) = \begin{cases}
1/\Delta_p & \text{for } x\in [0, \Delta_p] \\
0 & \text{else}
\end{cases}
{{< /m >}}

and

{{< m >}}
p(x) = \begin{cases}
1/\Delta_q & \text{for } x\in [0, \Delta_q] \\
0 & \text{else}.
\end{cases}
{{< /m >}}


{{< figure src="../assets/kl-divergence/kl-divergence-two-uniform.png" >}}

We will assume $\Delta_q > \Delta_p$ for simplicity. The KL divergence is

{{< m >}}
D_\text{KL}(p\parallel q) = \int_0^{\Delta_p} \frac{1}{\Delta_p}\log\left( \frac{1/\Delta_p}{1/\Delta_q} \right) dx +\int_{\Delta_p}^{\Delta_q}   \lim_{\epsilon\to 0} \epsilon \log\left( \frac{\epsilon}{1/\Delta_q} \right) dx,
{{< /m >}}

where the second term is 0. We have the KL divergence

{{< m >}}
D_\text{KL}(p\parallel q) = \log\left( \frac{\Delta_q}{\Delta_p} \right).
{{< /m >}}

The KL divergence is 0 if $\Delta_p = \Delta_q$, i.e., if the two distributions are the same.




## KL Divergence of Two Gaussians




Assuming the two distributions are two Gaussians $p(x)=\frac{1}{\sigma_p\sqrt{2\pi}} \exp\left( - \frac{ (x - \mu_p)^2 }{2\sigma_p^2} \right)$ and $q(x)=\frac{1}{\sigma_q\sqrt{2\pi}} \exp\left( - \frac{ (x - \mu_q)^2 }{2\sigma_q^2} \right)$, the KL divergence is

{{< m >}}
D_{\text{KL}}(p\parallel q) = \mathbb{E}_p \left[  \log \left(\frac{p}{q}\right)  \right].
{{< /m >}}

Notice that
{{< m >}}
\log \left( \frac{p}{q} \right) = \log \left( \exp\left(  - \frac{ (x - \mu_p)^2 }{2\sigma_p^2} + \frac{ (x - \mu_q)^2 }{2\sigma_q^2} \right) \right).
{{< /m >}}

As a simpler version of the problem, we assume that $\sigma_p = \sigma_q = \sigma$, so that

{{< m >}}
\log \left( \frac{p}{q} \right) =  \frac{ -(x - \mu_p)^2 + (x - \mu_q)^2  }{2\sigma^2} =  \frac{  \mu_q^2 - \mu_p^2}{2\sigma^2} + \frac{ (\mu_p  - \mu_q) x }{\sigma^2}.
{{< /m >}}

The KL divergence becomes

{{< m >}}
D_{\text{KL}} = \mathbb E_p \left[ \frac{  \mu_q^2 - \mu_p^2}{2\sigma^2} + \frac{ (\mu_p  - \mu_q) x }{\sigma^2} \right] = \frac{  \mu_q^2 - \mu_p^2}{2\sigma^2} + \frac{ (\mu_p  - \mu_q) }{\sigma^2} \mathbb E_p \left[ x \right] = \frac{  (\mu_q - \mu_p)^2}{2\sigma^2}.
{{< /m >}}

One could easily see that $\mathbb E_p \left[ x \right]=\mu$ using symmetries. The KL divergence for two Gaussians is symmetric for the distributions.

As an example, we calculate the KL divergence for the example shown in the figure.


{{< figure src="../assets/kl-divergence/two-gaussians.png" >}}


To get some intutions, we calculate the integrant $p(x)\log\left(p(x)/q(x)\right)$. The area under curve will be the KL divergence.




{{< figure src="../assets/kl-divergence/integrants.png" >}}



## KL Divergence is not necessarily symmetric

Using the uniform distribution example, we realize that

$$
D_\text{KL}(q\parallel p) \to \infty,
$$

which is very different from $D_\text{KL}(p\parallel q)$.


To illustrate the asymmetries using continuous , we will calculate the KL divergence of a Gaussian $p(x) =  \frac{1}{\sigma\sqrt{2\pi}} \exp\left( - \frac{ (x - \mu_{p})^2 }{2\sigma^2} \right)$ and a Guassian mixture $q(x)=\frac{1}{2\sigma\sqrt{2\pi}} \exp\left( - \frac{ (x - \mu_{q1})^2 }{2\sigma^2} \right) + \frac{1}{2\sigma\sqrt{2\pi}} \exp\left( - \frac{ (x - \mu_{q2})^2 }{2\sigma^2} \right)$. The KL divergence $D_{\text{KL}}(p \parallel q)$ is

$$
D_{\text{KL}}(p \parallel q) = \mathbb{E}_p \left[ \log\left( \frac{p}{q} \right) \right].
$$



{{< figure src="../assets/kl-divergence/guassian-mixture.png" >}}

We will calculate the integrants and area under curve will be the KL divergence $D_\text{KL}(p\parallel q)$.


{{< figure src="../assets/kl-divergence/guassian-mixture-integrants.png" >}}

The reverse KL divergence $D_\text{KL}(q\parallel p)$ is different.


{{< figure src="../assets/kl-divergence/guassian-mixture-integrants-d-q-p.png" >}}


The fact that KL divergence is not symmetric indicates that it can not be a distance measure.





[^Kurt2017]: {{< cite key="Kurt2017" >}}