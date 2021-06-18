---
title: "The Hubbard-Stratonovich Identity"
description: "Very useful in calculating the partition function"
date: 2021-06-17
category:
  - "Math"
references:
  - name: "Hubbard J. Calculation of Partition Functions. Physical Review Letters. 1959. pp. 77–78. doi:10.1103/physrevlett.3.77"
    link: "http://dx.doi.org/10.1103/physrevlett.3.77"
    key: "Hubbard1959"
tags:
  - "Linear Algebra"
  - "Calculus"
---


The Hubbard version of the Hubbard-Stratonovich identity is[^Hubbard1959]

{{< m >}}
\begin{align}
\exp{\left( a^2 \right)} =& \frac{1}{\sqrt{\pi}} \int_{-\infty}^\infty \mathrm dx\, \exp{ \left( - x^2 - 2 a x \right)}\\
 =& \frac{1}{\sqrt{\pi}} \int_{\infty}^{-\infty} \mathrm dx'\, \exp{ \left( - x'^2 + 2 a x' \right)},
\end{align}
{{< /m >}}

where we changed the sign of $x$, i.e., $x' = -x$.

In many partition functions, we have expressions like $\exp{\left( a^2/2\right)}$, using the identity, we have

{{< m >}}
\begin{align}
\exp{\left( \frac{a^2}{2} \right)} =& \frac{1}{\sqrt{\pi}} \int_{\infty}^{-\infty} \mathrm dx\, \exp{ \left( - x^2 + \sqrt{2} a x \right)} \\
=& \frac{1}{\sqrt{2\pi}} \int_{\infty}^{-\infty} \mathrm dx'\, \exp{ \left( - \frac{x'^2}{2} +  a x' \right)},
\end{align}
{{< /m >}}

where we define $x'=\sqrt{2}x$. We perform this transformation to get a kinetic energy like term.



[^Hubbard1959]: {{< cite key="Hubbard1959" >}}