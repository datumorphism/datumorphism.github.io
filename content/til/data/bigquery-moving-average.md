---
layout: til
title: "Calculate Moving Average Using SQL/BigQquery"
date: 2019-05-12
author: Lei Ma
comments: true
category:
- data
tags:
- Data Warehouse
- Big Query
- SQL
excerpt: Snippet for calculating moving avg using sql/biguqery
references:
- name: Getting table metadata using INFORMATION_SCHEMA
  link: https://cloud.google.com/bigquery/docs/information-schema-tables
---


Calculate moving avg using sql/biguqery

```SQL
AVG(users) OVER (ORDER BY day ROWS BETWEEN 6 PRECEDING AND 0 FOLLOWING) AS moving_avg
```

What about moving average for different categories? For examples, we have `date`, `categories`, `fee`. We would like to calculate the moving avg for each categories.

