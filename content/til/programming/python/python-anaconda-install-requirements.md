---
layout: til
title: "Installing requirements.txt in Conda Environments"
date: 2019-03-13
author: Lei Ma
category:
- programming
- basics
tags:
- Python
- Anaconda
references:
  - name: "Use 'pip install' in the virtual environment created by conda"
    link: https://github.com/ContinuumIO/anaconda-issues/issues/1429
summary: Why is pip install -r requirements.txt not working?
---

It is quite common to use `requirements.txt` to specify the python package requirements for the project. What is usually done is

```
pip install -r requirements.txt
```

When we create a new conda environment using

```
conda create --name my_project_env
```

`pip` is not installed by default. However, pip is usually installed on a user level, which means you could run the command

```
pip install -r requirements.txt
```

in this environment. But this will install all requirements to the python path globally instead of in the environment.


To install `requirements.txt` in the environment, we have to use the `pip` installed within the environment. Thus we should install `pip` first by

```
conda install pip
```

Then we can install the requirements.txt.


Of course, there is a better way. We simply create a conda environment with `pip` installed in it:

```
conda create -n yourenv pip
```

