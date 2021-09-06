---
title: "Jensen-Shannon Divergence"
description: ""
date: 2021-09-04
authors:
  - "Lei Ma"
categories:
  - "Information"
tags:
  - "Information Theory"
  - "Divergence"
references:
  - name: "Contributors to Wikimedia projects. Jensen–Shannon divergence. In: Wikipedia [Internet]. 15 Jun 2021 [cited 6 Sep 2021]. Available: https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence"
    link: "https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence"
    key: "jensen-shannon_divergence_wiki"
links:
  - "wiki/machine-learning/basics/kl-divergence.md"
---

The Jensen-Shannon divergence is a symmetric divergence of distributions $P$ and $Q$,

{{< m >}}
\operatorname{D}_{\text{JS}} = \frac{1}{2} \left[ \operatorname{D}_{\text{KL}} \left(P \bigg\Vert \frac{P+Q}{2} \right) +  \operatorname{D}_{\text{KL}} \left(Q \bigg\Vert \frac{P+Q}{2}\right) \right],
{{< /m >}}

where $\operatorname{D}_{\text{KL}}$ is the {{< c "wiki/machine-learning/basics/kl-divergence.md" "KL Divergence" >}}.



[^jensen-shannon_divergence_wiki]: {{< cite key="jensen-shannon_divergence_wiki" >}}
