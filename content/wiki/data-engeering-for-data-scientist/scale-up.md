---
title: "Scale Up"
description: "scale up your services"
date: "2021-05-05"
category:
  - "Data Engineering"
tags:
  - "Data Engineering"
  - "Data Storage"
references:
  - name: "The Data Engineering Cookbook"
    link: "https://github.com/andkret/Cookbook"
    key: "Kretz2019"
supplementary:
  - name: "The Data Engineering Cookbook"
    link: "https://github.com/andkret/Cookbook"
weight: 40
---

{{< message class="warning" >}}
Many of the example are from the book by Adreas Kretz. Find the link to the book in the references section.
{{< /message >}}


## Scaling Up Storage


### Scaling Up SQL DB


#### SAN: Storage Area Network


Use multiple servers on the DB storage to make the query faster.

- Good for Read-only DB
- Not convinient to update DB


### Hadoop


Hadoop:

- Distributed storage
- Analysis

4 core modules:

- Hadoop common
  - background functionalities
- HDFS
  - Divide into blocks
  - Distribute
- MapReduce
  - Old tech
- YARN
  - Resource management


The Hadoop Ecosystem:

- Many tools that can be connected to Hadoop or are based on Hadoop
- Not only about the 4 core modules anymore if we consider the ecosystem:
  - Spark is also using YARN
- No need to use everything in Hadoop
  - Data->(Kafka->Spark)->DB
    - The (*) can be using Hadoop


{{< figure src="../assets/scale-up/hadoop-ecosystem.png" caption="Adapted from https://github.com/andkret/Cookbook" >}}






