---
title: "Generate a Column of Continuous Dates in BigQuery"
date: 2019-05-12
authors:
  - Lei Ma
categories:
  - data
tags:
  - Data Warehouse
  - Big Query
summary: Generate a table with a column of continuous dates
---



```SQL
SELECT
  *
FROM
  UNNEST( GENERATE_DATE_ARRAY( CURRENT_DATE(), DATE('2014-01-01'), INTERVAL -1 DAY) ) AS day
```

