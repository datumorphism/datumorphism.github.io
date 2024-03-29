---
title: "PyTorch: Initialize Parameters"
date: 2021-01-01
authors:
  - Lei Ma
categories:
  - machine-learning
tags:
  - Python
  - PyTorch
references:
  - name: "Lippe P. Tutorial 3: Activation Functions — UvA DL Notebooks v1.1 documentation. In: UvA Deep Learning Tutorials [Internet]. [cited 23 Sep 2021]. Available: https://uvadlc-notebooks.readthedocs.io"
    link: "https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial3/Activation_Functions.html"
    key: "Lippe"
links:
  - "cards/machine-learning/neural-networks/neural-networks-initialization.md"
---


We can set the parameters in a for loop. We take some of the initialization methods from Lippe[^Lippe].

To set based on the input dimension of the layer ({{< c "cards/machine-learning/neural-networks/neural-networks-initialization.md" >}}) (**normalized initialization**),


```python
for name, param in model.named_parameters():
    if name.endswith(".bias"):
        param.data.fill_(0)
    else:
        bound = math.sqrt(6)/math.sqrt(param.shape[0]+param.shape[1])
        param.data.uniform_(-bound, bound)
```

or set the parameters based on the input size of each layer

```python
for name, param in model.named_parameters():
        if name.endswith(".bias"):
            param.data.fill_(0)
        else:
            param.data.normal_(std=1.0/math.sqrt(param.shape[1]))
```

or set the params to some fixed normal distribution

```python
some_std = 0.1
for name, param in model.named_prameters():
    param.data.normal_(std=some_std)
```

or be constant if we really want,

```python
some_value = 0.1
for name, param in model.named_prameters():
    param.data.fill_(some_value)
```


For different activation functions, the factor for $1/D$, with $D$ being the dimension of the input, can be different. Use `torch.nn.init.calculate_gain`.


[^Lippe]: {{< cite key="Lippe" >}}