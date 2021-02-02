---
title: "Data File Formats"
description: ""
date: 2021-02-02
authors:
  - "LM"
categories:
  - "data science"
tags:
  - data
  - data-engineering
  - data-science
references:
  - name: "Parquet Logical Type Definitions"
    link: "https://github.com/apache/parquet-format/blob/master/LogicalTypes.md"
  - name: "Working with Complex Data Formats with Structured Streaming in Apache Spark 2.1 Part 2 of Scalable Data @ Databricks"
    link: "https://databricks.com/blog/2017/02/23/working-complex-data-formats-structured-streaming-apache-spark-2-1.html"
weight:
links:
  - "cards/machine-learning/datatypes/data-types.md"
---


Data storage is diverse. For data on smaller scales, we are mostly dealing with some data files.

![](../assets/work_with_data_files.png)


[work_with_data_files](../assets/work_with_data_files.pdf)


## Efficiencies and Compressions

![](../assets/read-storage-performance-scatter-plot.png)



### Parquet

Parquet is fast. But

1. Don't use json or list of json as columns. Convert them to strings or binary objects if it is really needed.



