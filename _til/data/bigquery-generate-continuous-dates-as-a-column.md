---
layout: til
title: "Generate a Column of Continuous Dates in BigQuery"
date: 2019-05-12
author: Lei Ma
comments: true
category:
- data
tag:
- Data Warehouse
- Big Query
excerpt: Generate a table with a column of continuous dates
---



```SQL
SELECT
  *
FROM
  UNNEST( GENERATE_DATE_ARRAY( CURRENT_DATE(), DATE('2014-01-01'), INTERVAL -1 DAY) ) AS day
```

