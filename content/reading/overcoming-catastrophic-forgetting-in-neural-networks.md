---
title:  "Overcoming catastrophic forgetting in neural networks"
date: 2017-05-14 #2014-08-27T11:57:41-04:00
modified: 2017-05-14
subtitle: ""
speaker: "Lei Ma"
authors:
  - Lei Ma
categories:
  - theory
tags:
  - 'neural network'
summary: "Using a newly defined loss function the authors could implement an idea that achieves the multi-task within one network."
status: Done
references:
  - name: "Overcoming catastrophic forgetting in neural networks"
    link: http://www.pnas.org/content/114/13/3521
---


## The General Idea

During the training of neural networks, the previous tasks would be forgotten significantly if completely new types of data are fed to the network. This is dubbed as **catastrophic forgetting**.

Naively speaking, the way to overcome this forgetting is to either keep some of the structure in the network or feed the previous data sets together with the new ones. Most of the time the second methods doesn't make sense since it requires larger overall data set as new tasks are added which consumes more computation resources. The authors use the first method.

## The Loss Function

To achieve this, they defined a loss function at step i

$$
\mathscr L_i = \frac{1}{2}\left( ( W_i x_i - y_i )^2 + \lvert W_i - W_{i-1} \rvert_{M_i}  \right),
$$

where $W_i$ is the weight at step i. The last term is the distance between the weight of the current step and the previous step. Such a loss function requires that the weight in the new steps should NOT change all the weights a lot.

During a minimization of the new step of training, a traditional method is to minimize $( W_i x_i - y_i )^2$. However, if such a minimization changes too many weights by a large amount, the new loss function $\mathscr L_i$ would be very large and becomes unacceptable. Thus the minimization of the new loss requires the network to use most of the weights in the previous steps while completing the new task.

The term $\lvert W_i - W_{i-1} \rvert_{M_i}$ is the distance and can be any form that has the meaning of distance. The author tested diagonal elements of Fisher matrix which works well.

## Bayesian Analysis

The previous statements contain an assumption that the network has enough degrees of freedom to perform all the tasks. In other words, there exists different sets of parameters that can lead to the same results.

The Bayesian theorem tells us that

$$
P(A\vert B) P(B) = P(B\vert A)P(A),
$$

which has a log form

$$
\log( P(A\vert B) ) = \log( P(B\vert A) ) + \log(P(A)) - \log(P(B)).
$$

Back the neural networks, the set of weights $\theta = \{W_i\}$ are the variables to calculate and the prior is the data set $D$. The Bayesian theorem becomes

$$
\log( P(\theta\vert D) ) = \log( P(D\vert \theta) ) + \log(P(\theta)) - \log(P(D)).
$$

For given parameters the calculation probability of data is described by $\log( P(D\vert \theta) )$, which is related to the loss function. This equation says that to calculate the weights for given data set we need to calculate the loss function as well as the priors, in theory.

For two data sets $D_A$ and $D_B$,

$$
\log( P(\theta\vert \{D_A , D_B\}) ) = \log( P(D_B \vert \theta) ) \log( P(\theta\vert D_A)) - \log( P(D_B) ).
$$

$\log( P(\theta\vert D_A , D_B) )$ tells us about the weights for both data sets. $\log( P(D_B\vert\theta)) $ is the loss function of the second data set $B$. When two data sets are considered we have to consider the weights trained from the first data set.

As we have seen, this can be achieved by defining a new loss function that contains the change of weights.


## So?

For a very high dimensional parameter space, the land scape probably has multiple possible configurations that can help to complete one task. The most efficient way to really develop a multi-task network is to find the common configuration for all the data sets. It seems to be hard if we don't train them simultaneously. The method the author used is one of the ways but it is a compromise and doesn't guarantee a common configuration.

I would be convinced that this is a good method until it can be proven that it selects out the most important weights and fixed them (dropout).
