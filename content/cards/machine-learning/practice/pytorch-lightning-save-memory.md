---
title: "PyTorch Lightning Save Memory"
description: "Tips to save memory in pytorch lightning"
date: 2022-09-06T08:09:26+02:00
authors:
  - "L Ma"
categories:
  - "ML Practice"
tags:
  - "Machine Learning"
  - "PyTorch Lightning"
garden:
  - "seedling"
published: false
---


A few tips on saving memory in pytorch lightning.

## DataModule

Do not load the full dataset in DataModule `__init__`.

## Trainer

Set `return_prediction=False` to avoid accumulating predictions in memory.
