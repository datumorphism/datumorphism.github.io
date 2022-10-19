---
title: "CUDA Memory"
description: "Optimizing memory operations for CUDA"
date: 2022-10-19
authors:
  - "L Ma"
categories:
  - "ML Practice"
tags:
  - "CUDA"
references:
  - name: "Mohan A. Pipelining data processing and host-to-device data transfer. In: Telesens [Internet]. [cited 17 Oct 2022]. Available: https://www.telesens.co/2019/02/16/efficient-data-transfer-from-paged-memory-to-gpu-using-multi-threading/"
    link: "https://www.telesens.co/2019/02/16/efficient-data-transfer-from-paged-memory-to-gpu-using-multi-threading/"
    key: "Mohan2019"
  - name: "Harris M. How to Optimize Data Transfers in CUDA C/C++. In: NVIDIA Technical Blog [Internet]. 5 Dec 2012 [cited 19 Oct 2022]. Available: https://developer.nvidia.com/blog/how-optimize-data-transfers-cuda-cc/"
    link: "https://developer.nvidia.com/blog/how-optimize-data-transfers-cuda-cc/"
    key: "Harris2012"
  - name: "Contributors to Wikimedia projects. Memory paging. In: Wikipedia [Internet]. 7 Oct 2022 [cited 19 Oct 2022]. Available: https://en.wikipedia.org/wiki/Memory_paging"
    link: "https://en.wikipedia.org/wiki/Memory_paging"
  - name: "Computer Science. Segmented, Paged and Virtual Memory. YouTube. 2019. Available: https://www.youtube.com/watch?v=p9yZNLeOj4s"
    link: "https://www.youtube.com/watch?v=p9yZNLeOj4s"
  - name: "CoffeeBeforeArch. CUDA Crash Course (v2): Pinned Memory. YouTube. 2019. Available: https://www.youtube.com/watch?v=ShT7raBPP8k"
    link: "https://www.youtube.com/watch?v=ShT7raBPP8k"
  - name: "torch.utils.data — PyTorch 1.8.1 documentation. [cited 19 Oct 2022]. Available: https://pytorch.org/docs/1.8.1/data.html#memory-pinning"
    link: "https://pytorch.org/docs/1.8.1/data.html#memory-pinning"
    key: "pytorch-memory-pinning"
  - name: "Mao L. Page-Locked Host Memory for Data Transfer. In: Lei Mao’s Log Book [Internet]. 26 Jun 2021 [cited 19 Oct 2022]. Available: https://leimao.github.io/blog/Page-Locked-Host-Memory-Data-Transfer/"
    link: "https://leimao.github.io/blog/Page-Locked-Host-Memory-Data-Transfer/"
  - name: "Gao Y. What is the disadvantage of using pin_memory? In: PyTorch Forums [Internet]. 6 Apr 2017 [cited 19 Oct 2022]. Available: https://discuss.pytorch.org/t/what-is-the-disadvantage-of-using-pin-memory/1702"
    link: "https://discuss.pytorch.org/t/what-is-the-disadvantage-of-using-pin-memory/1702/2"
    key: "smth-pinned-memory"
garden:
  - "seedling"
---

[CUDA](https://en.wikipedia.org/wiki/CUDA) is widely used in deep learning. Though many of deep learning professionals are not exposed to CUDA directly, most people are already using CUDA as frameworks like PyTorch are providing GPU support through CUDA.

To optimize the computational efficiency of our models, knowledge about the data transfer inside the devices is crucial. In this note, we build up the fundamentals of memory transfer for CUDA.

## Segmented Memory and Paged Memory

{{< youtube p9yZNLeOj4s >}}


## CUDA Can not Use Paged Memory

A CPU host uses paged memory. However, GPU can not directly take data from paged memory on the host[^Harris2012]. Before accessing the data, CUDA has to pin the memory so that the memory is page-locked[^pytorch-memory-pinning]. Pinned memory stays on the physical memory and won't be moved to secondary memory so that GPU doesn't need CPU to page-in/out memory.

{{< figure src="../assets/cuda-memory/cuda-pagable-pin.jpg" caption="Harris M. How to Optimize Data Transfers in CUDA C/C++. In: NVIDIA Technical Blog [Internet]. 5 Dec 2012 [cited 19 Oct 2022]. Available: https://developer.nvidia.com/blog/how-optimize-data-transfers-cuda-cc/" >}}


## Pinned Memory is Fast

I took two screenshots from [a video by CoffeeBeforeArch](https://www.youtube.com/watch?v=ShT7raBPP8k).


{{< figure src="../assets/cuda-memory/cuda-pagable.png" title="Unpinned Momory" caption="CoffeeBeforeArch. CUDA Crash Course (v2): Pinned Memory. YouTube. 2019. Available: https://www.youtube.com/watch?v=ShT7raBPP8k" >}}
{{< figure src="../assets/cuda-memory/cuda-pinned.png" title="Pinned Memory" caption="CoffeeBeforeArch. CUDA Crash Course (v2): Pinned Memory. YouTube. 2019. Available: https://www.youtube.com/watch?v=ShT7raBPP8k" >}}

## Why don't we pin memory all the time in PyTorch DataLoader

The [`DataLoader`](https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader) in PyTorch provide the option `pin_memory`. By default this option is set to `False`. It is tempting to set this to `True` all the time.

However, memory pinning also [takes time and computing capacity](https://www.telesens.co/2019/02/16/efficient-data-transfer-from-paged-memory-to-gpu-using-multi-threading/#Dataloader_in_PyTorch_10), and may cause issues[^Mohan2019][^smth-pinned-memory].


[^Harris2012]: {{< cite key="Harris2012" >}}
[^pytorch-memory-pinning]: {{< cite key="pytorch-memory-pinning" >}}
[^Mohan2019]: {{< cite key="Mohan2019" >}}
[^smth-pinned-memory]: {{< cite key="smth-pinned-memory" >}}
