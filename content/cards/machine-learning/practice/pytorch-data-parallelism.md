---
title: "Pytorch Data Parallelism"
description: "Data parallelism in pytorch"
date: 2022-10-19T14:54:29+02:00
authors:
  - "L Ma"
categories:
  - "ML Practice"
tags:
  - "PyTorch"
  - "Parallel"
references:
  - name: "Wolf T. 💥 Training Neural Nets on Larger Batches: Practical Tips for 1-GPU, Multi-GPU & Distributed setups. HuggingFace. 2 Sep 2020. Available: https://medium.com/huggingface/training-larger-batches-practical-tips-on-1-gpu-multi-gpu-distributed-setups-ec88c3e51255. Accessed 19 Oct 2022."
    link: "https://medium.com/huggingface/training-larger-batches-practical-tips-on-1-gpu-multi-gpu-distributed-setups-ec88c3e51255"
    key: "Wolf2020"
  - name: "Mao L. Data Parallelism VS Model Parallelism in Distributed Deep Learning Training. In: Lei Mao’s Log Book [Internet]. 23 May 2019 [cited 19 Oct 2022]. Available: https://leimao.github.io/blog/Data-Parallelism-vs-Model-Paralelism/"
    link: "https://leimao.github.io/blog/Data-Parallelism-vs-Model-Paralelism/"
    key: "Mao2019"
  - name: "Effective Training Techniques — PyTorch Lightning 1.7.7 documentation. In: PyTorch Lightning [Internet]. [cited 19 Oct 2022]. Available: https://pytorch-lightning.readthedocs.io/en/stable/advanced/training_tricks.html#accumulate-gradients"
    link: "https://pytorch-lightning.readthedocs.io/en/stable/advanced/training_tricks.html#accumulate-gradients"
    key: "pytorch-lightning-tricks"
  - name: "Jia Z, Zaharia M, Aiken A. Beyond Data and Model Parallelism for Deep Neural Networks. arXiv [cs.DC]. 2018. Available: http://arxiv.org/abs/1807.05358"
    link: "http://arxiv.org/abs/1807.05358"
    key: "Jia2018"
  - name: "Li X, Zhang G, Li K, Zheng W. Chapter 4 - Deep Learning and Its Parallelization. In: Buyya R, Calheiros RN, Dastjerdi AV, editors. Big Data. Morgan Kaufmann; 2016. pp. 95–118. doi:10.1016/B978-0-12-805394-2.00004-0"
    link: "https://www.sciencedirect.com/science/article/pii/B9780128053942000040"
    key: "Li2016"
  - name: "Xiandong. Intro Distributed Deep Learning. In: Xiandong [Internet]. 13 May 2017 [cited 19 Oct 2022]. Available: https://xiandong79.github.io/Intro-Distributed-Deep-Learning"
    link: "https://xiandong79.github.io/Intro-Distributed-Deep-Learning"
    key: "Xiandong2017"
  - name: "Mohan A. Distributed data parallel training using Pytorch on AWS. In: Telesens [Internet]. [cited 17 Oct 2022]. Available: https://www.telesens.co/2019/04/04/distributed-data-parallel-training-using-pytorch-on-aws/"
    link: "https://www.telesens.co/2019/04/04/distributed-data-parallel-training-using-pytorch-on-aws/"
    key: "Mohan2019"
  - name: "Writing Distributed Applications with PyTorch — PyTorch Tutorials 1.12.1+cu102 documentation. In: PyTorch [Internet]. [cited 19 Oct 2022]. Available: https://pytorch.org/tutorials/intermediate/dist_tuto.html#collective-communication"
    link: "https://pytorch.org/tutorials/intermediate/dist_tuto.html#collective-communication"
    key: "pytorch-dist_tuto"
  - name: "Getting Started with Distributed Data Parallel — PyTorch Tutorials 1.12.1+cu102 documentation. In: PyTorch [Internet]. [cited 19 Oct 2022]. Available: https://pytorch.org/tutorials/intermediate/ddp_tutorial.html"
    link: "https://pytorch.org/tutorials/intermediate/ddp_tutorial.html"
    key: "pytorch-ddp-tutorial"
links:
  - "cards/machine-learning/practice/cuda-memory.md"
garden:
  - "seedling"
---


To train large models using PyTorch, we need to go parallel. There are two commonly used strategies[^Jia2018][^Xiandong2017][^Mao2019]:

1. model parallelism,
2. data parallelism,
3. data-model parallelism.

## Model Parallelism

Model parallelism splits the model on different nodes[^Jia2018][^Li2016]. We will focus on data parallelism but the key idea is shown in the following illustration.

{{< figure src="../assets/pytorch-data-parallelism/model-parallelism.png" title="Model parallel" caption="Li X, Zhang G, Li K, Zheng W. Chapter 4 - Deep Learning and Its Parallelization. In: Buyya R, Calheiros RN, Dastjerdi AV, editors. Big Data. Morgan Kaufmann; 2016. pp. 95–118. doi:10.1016/B978-0-12-805394-2.00004-0" >}}

## Data Parallelism

Data parallelism creates replicas of the model on each device and use different subsets of training data[^Jia2018][^Li2016].

{{< figure src="../assets/pytorch-data-parallelism/data-parallelism.png" title="Data parallelism" caption="Li X, Zhang G, Li K, Zheng W. Chapter 4 - Deep Learning and Its Parallelization. In: Buyya R, Calheiros RN, Dastjerdi AV, editors. Big Data. Morgan Kaufmann; 2016. pp. 95–118. doi:10.1016/B978-0-12-805394-2.00004-0" >}}

Data parallelism is based on the additive property of the loss gradient.

There are two ready to use data parallel paradigms: DataParallel and [DistributedDataParallel](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html).


### Jargons

To better understand what happens in the strategies, we recommend reading the following.

- {{< e "cards/machine-learning/practice/cuda-memory.md" >}}
- The PyTorch documentation provides an illustration on [collective communication](https://pytorch.org/tutorials/intermediate/dist_tuto.html#collective-communication).


### `DataParallel` in PyTorch

[`DataParallel`](https://pytorch.org/docs/stable/generated/torch.nn.DataParallel.html#torch.nn.DataParallel) is a strategy [implemented in PyTorch](https://pytorch.org/tutorials/beginner/blitz/data_parallel_tutorial.html?highlight=dataparallel) using multi-threading.


{{< figure src="../assets/pytorch-data-parallelism/data-parallel-mohan.png" title="DataParallel" caption="Mohan A. Distributed data parallel training using Pytorch on AWS. In: Telesens [Internet]. [cited 17 Oct 2022]. Available: https://www.telesens.co/2019/04/04/distributed-data-parallel-training-using-pytorch-on-aws/" >}}

The above illustration shows that the master GPU, "GPU 0", is the coordinator and also computes more than others. This creates imbalance in GPU usage.

Due to multi-threading, `DataParallel` also suffers from [GIL](https://realpython.com/python-gil/)[^pytorch-ddp-tutorial].


### `DistributedDataParallel` in PyTorch

[`DistributedDataParallel`](https://pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel) (DDP) is a strategy [implemented in PyTorch](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html) using {{< c "wiki/programming-languages/python/multiprocessing.md" "multi-processing" >}}. DDP is the recommended method in the PyTorch documentation.

{{< figure src="../assets/pytorch-data-parallelism/distributed-data-parallel-mohan.png" title="Distributed DataParallel" caption="Mohan A. Distributed data parallel training using Pytorch on AWS. In: Telesens [Internet]. [cited 17 Oct 2022]. Available: https://www.telesens.co/2019/04/04/distributed-data-parallel-training-using-pytorch-on-aws/" >}}




[^Jia2018]: {{< cite key="Jia2018" >}}
[^Xiandong2017]: {{< cite key="Xiandong2017" >}}
[^Mao2019]: {{< cite key="Mao2019" >}}
[^Li2016]: {{< cite key="Li2016" >}}
[^pytorch-ddp-tutorial]: {{< cite key="pytorch-ddp-tutorial" >}}