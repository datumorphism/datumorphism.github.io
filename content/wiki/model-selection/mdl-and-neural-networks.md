---
title: MDL and Neural Networks
date: 2021-02-14
categories:
  - Model Selection
tags:
  - Model Selection
  - Neural Network
  - MDL
references:
  - link: "https://doi.org/10.1145/168304.168306"
    name: "Hinton, G. E., & van Camp, D. (1993). Keeping the neural networks simple by minimizing the description length of the weights. Proceedings of the Sixth Annual Conference on Computational Learning Theory - COLT 93, 5–13."
    key: "Hinton1993"
  - link: "https://mbernste.github.io/posts/sourcecoding/#:~:text=Shannon's%20Source%20Coding%20Theorem%20tells,to%20unambiguously%20communicate%20those%20samples.&text=In%20this%20post%2C%20we%20will%20walk%20through%20Shannon's%20theorem."
    name: "Shannon’s Source Coding Theorem (Foundations of information theory: Part 3)"
links:
  - cards/information/coding-theory-concepts.md
  - wiki/model-selection/measures-of-generalizability.md
  - wiki/model-selection/goodness-of-fit.md
  - cards/statistics/mdl.md
weight: 5
---

Minimum Description Length ({{< c "cards/statistics/mdl.md" "MDL" >}}) can be used to construct a concise network. A fully connected network has great expressing power but it is easily overfitting.

One strategy is to apply constraints to the networks:
- Limit the connections;
- Shared weights in subgroups of the network;
- Constrain the weights using some probability distributions.


By minimizing the MDL of the network and the misfits on the data, we can build a concise network. Based on the {{< c "cards/information/coding-theory-concepts.md" "Source Coding Theorem" >}}, we can encode the misfit and the model using Shannon information content [^Hinton1993]. The description length for the misfit and the model corresponds to the Shannon information content. Thus we can define an expected description length and minimize it in the model so that we can balance the complexity of the model and the goodness of fit.



[^Hinton1993]: {{< cite key="Hinton1993" >}}

