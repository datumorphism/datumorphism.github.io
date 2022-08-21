---
title: "Dilated Convolution"
description: ""
date: 2022-08-21T16:03:14+02:00
authors:
  - "Lei Ma"
categories:
  - "Math"
tags:
  - "Convolution"
references:
  - name: "Yu F, Koltun V. Multi-Scale Context Aggregation by Dilated Convolutions. arXiv [cs.CV]. 2015. Available: http://arxiv.org/abs/1511.07122"
    link: "http://arxiv.org/abs/1511.07122"
    key: "Yu2015"
garden:
  - "seedling"
---

For a convolution

{{< m >}}
f*h(x) = \sum_{s+t=x} f(s) h(t),
{{< /m >}}

the dilated version of it is[^Yu2015]

{{< m >}}
f*_l h(x) = \sum_{s+t*l=x} f(s) h(t),
{{< /m >}}

where $l$ is the dilation factor.


[^Yu2015]: {{< cite key="Yu2015" >}}
