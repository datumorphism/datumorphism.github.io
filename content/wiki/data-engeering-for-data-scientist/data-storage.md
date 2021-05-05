---
title: "Data Storage"
description: "Storing big data"
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
weight: 10
---

{{< message class="warning" >}}
Many of the example are from the book by Adreas Kretz. Find the link to the book in the references section.
{{< /message >}}


## Types of Storage and Data

Here is a list [^Kretz2019]

- Files
  - S3
- Message Queues
  - Kinesis
- Relational DB
  - MySQL
  - Postgres
- Non-relational DB
  - Document Store
    - MongoDB
    - DocumentDB
  - Key-Value Store
    - HBase
    - Redis

[^Kretz2019]: {{< cite key="Kretz2019" >}}