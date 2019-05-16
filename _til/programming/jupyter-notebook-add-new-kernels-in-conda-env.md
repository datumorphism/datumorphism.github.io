---
layout: til
title: "Add New Kernels to Jupyter Notebook in Conda Environment"
date: 2019-05-12
author: Lei Ma
comments: true
category:
- programming
tag:
- Python
- Jupyter
excerpt: Python package or python module autoreloading in jupyter notebook
---

When we fire up our jupyter notebook/lab, we might find that jupyter doesn't load python kernels of conda environments by default. This is usually because the conda environment doesn't have a ipykernel to be loaded by jupyter.

If you would like to add some of your conda environments to your jupyter notebook/lab, install `ipykernel` in your conda environment (e.g., your_env).

```bash
(your_env)$ conda install ipykernel
(your_env)$ ipython kernel install --user --name=<any_name_for_kernel>
(your_env($ conda deactivate
```

More can be found in the documentation ( [ipython](https://ipython.readthedocs.io/en/latest/install/kernel_install.html), [jupyter](https://jupyter.readthedocs.io/en/latest/install-kernel.html) ).

