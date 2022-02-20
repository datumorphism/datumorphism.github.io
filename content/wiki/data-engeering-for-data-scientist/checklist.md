---
title: "Data Engineering for Data Scientists: Checklist"
description: "A checklist to get a shallow understanding of the basics and the ecosystem"
date: "2021-05-05"
categories:
  - "Data Engineering"
tags:
  - "Data Engineering"
references:
  - name: "The Data Engineering Cookbook"
    link: "https://github.com/andkret/Cookbook"
    key: "Kretz2019"
weight: 1
links:
  - "wiki/data-engeering-for-data-scientist/data-processing.md"
  - "wiki/data-engeering-for-data-scientist/data-storage.md"
  - "wiki/data-engeering-for-data-scientist/scale-up.md"
---

It is always good for a data scientist to understand more about data engineering, especially the blueprint of a fully productionized data platform.

There are several things to get into:

- Connection to Data Sources
  - Connect to DB
  - Connect to Streaming Data
    - Message Queues
  - Connect to Website
    - Scraping
      - {{< c "wiki/nodecrawler/" >}}
    - API
  - Other Data Services
- {{< c "wiki/data-engeering-for-data-scientist/data-storage.md" "Data Storage" >}}
  - Data Lake
  - {{< c "wiki/data-warehouse/" >}}
  - Message Queues
- {{< c "wiki/data-engeering-for-data-scientist/data-processing.md" "Data Processing" >}}
  - Streaming
  - Batch Processing
- Data Buffer
  - Cache:
    - Redis
      - {{< c "wiki/computation/basics-of-redis.md" >}}
  - Message Queues
    - Kafka
    - AWS Kinesis
- Using Data
  - Query Data
  - Visualization
  - Analysis and Model Building
- {{< c "wiki/data-engeering-for-data-scientist/scale-up.md" "Scale Up" >}}
  - Scale up storage
  - Scale up node
  - Parallel