---
title: "Data Processing"
description: "Processing Data is essential."
date: "2021-05-05"
category:
  - "Data Engineering"
tags:
  - "Data Engineering"
references:
  - name: "The Data Engineering Cookbook"
    link: "https://github.com/andkret/Cookbook"
    key: "Kretz2019"
supplementary:
  - name: "The Data Engineering Cookbook"
    link: "https://github.com/andkret/Cookbook"
weight: 20
---

{{< message class="warning" >}}
Many of the example are from the book by Adreas Kretz. Find the link to the book in the references section.
{{< /message >}}


## Batch Process

Kretz recommend to start from batch processing and move to streaming if needed [^Kretz2019].


## Stream Process


Three methods to stream data

- At Least Once: 
  - message gets processed once or multiple times
never dropped
  - e.g., time-based GPS data in fleet management, if the stream data has the same timestamp, then we just override the existing data, we do not care how many times the data is being processed or streamed.
- At Most Once:
  - okay to drop a message
  - only processed once at max
  - e.g. accident events, do not record multiple times otherwise it is gonna be a misleading signal that the accident happens a lot.
- Exactly Once:
  - do not drop message
  - e.g., banking


## Tools


### Spark

Spark is in-memory storage.

- e.g., Load from HDFS to memory of workers,
- input data and intermediate results are in memory, no disk writes,
- no clear map-reduce stage anymore,
- can be complex analysis,
- supports streaming analysis,
- native support for scheduling jobs.


{{< figure src="../assets/data-processing/spark-and-hadoop.png" caption="This figure is a screenshot from the book by [Adreas Kretz](https://github.com/andkret/Cookbook)." >}}



#### RDD

Resilient Distributed Datasets (RDD) is the core of Spark.

- Similar to Map-Reduce
- Lower level
- Old stuff
- Now dataframes/datasets

#### DataFrames

DataFrames is the successor to RDD.



#### SparkSQL

SparkSQL is used to access dataframes.



#### Run Complex Models in Spark

One could run complex machine learning models directly on Spark using tools such as Tensorflow and MLlib.



#### Resource management

Spark has its own resource management module. But one could also use Hadoop's YARN.


#### When to use Spark

If the processing is simple (summing, counting, etc): Map-reduce is good enough

If the analytics is complex (ML) or need speed: Spark



#### Spark + Hadoop

e.g, use YARN to manage physical resources. 

If Spark and Hadoop is running on the same workers, doesn't make sense to have multiple resource managers. In this case, use Hadoop's YARN.



#### Use Data from Hadoop

Use the local Hadoop data in Spark

{{< figure src="../assets/data-processing/using-data-from-spark.png" caption="This figure is a screenshot from the book by [Adreas Kretz](https://github.com/andkret/Cookbook)." >}}


### Flink

[Docs](https://flink.apache.org/)

{{< figure src="../assets/data-processing/flink-home-graphic.png" caption="From the website of Apache Flink" >}}


- Stateful Computations
- Event-driven applications
- Stream and Batch analysis
- ETL














[^Kretz2019]: {{< cite key="Kretz2019" >}}