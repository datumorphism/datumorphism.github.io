---
layout: til
title: "Installing requirements.txt in Conda Environments"
date: 2019-03-13
author: Lei Ma
categories:
- programming
- basics
tags:
- Python
- Anaconda
references:
  - name: "Use 'pip install' in the virtual environment created by conda"
    link: "https://github.com/ContinuumIO/anaconda-issues/issues/1429"
  - name: "Managing environments — conda documentation."
    link: "https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#id2"
summary: Why is pip install -r requirements.txt not working in conda?
links:
  - tags/python
  - til/programming/jupyter-notebook-add-new-kernels-in-conda-env.md
---

It is quite common to use `requirements.txt` to specify the python package requirements for the project. What is usually done is

```bash
pip install -r requirements.txt
```

## The Problem with Conda

When we create a new conda environment using

```bash
conda create --name my_project_env
```

`pip` is not installed by default. However, pip is usually installed on a user level, which means you could run the command

```bash
pip install -r requirements.txt
```

in this environment. But this will install all requirements to the python path globally instead of in the environment.


{{< card title="Check which pip" class="warning" >}}

One could check the current pip using the following command

```bash
which pip
```

For example, one could get this result

```text
/Users/itsme/anaconda3/bin/pip
```

If the above is the what you get, then it is likely that you are not using the `pip` in your environment.

Suppose you have an environment named `amneumarkt`, `which pip` should show something like the following.

```text
/Users/itsme/anaconda3/envs/amneumarkt/bin/pip
```

{{< /card >}}

## How to do it

To install `requirements.txt` in the environment, we have to use the `pip` installed within the environment. Thus we should install `pip` first by

```bash
conda install pip
```

Then we can install the requirements.txt.


Of course, there is a better way. We simply create a conda environment with `pip` installed in it:

```bash
conda create -n yourenv pip
```

Or if you want to specify your python version for this conda environment,

```bash
conda create -n python=3.7 yourenv pip
```

## Using environment.yml instead of requirements.txt

Refer to the documentation: [Creating an environment from an environment.yml file](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)