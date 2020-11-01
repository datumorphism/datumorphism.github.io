---
layout: til
title: "BigQuery Meta Tables"
date: 2019-05-12
author: Lei Ma
comments: true
category:
- data
tags:
- Data Warehouse
- Big Query
summary: Meta tables are very useful when it comes to get bigquery table information programmatically.
references:
- name: Getting table metadata using INFORMATION_SCHEMA
  link: https://cloud.google.com/bigquery/docs/information-schema-tables
---

In BigQuery, there are meta tables that we can use to retrieve information about the dataset and tables.


```SQL
#standardSQL
SELECT
*
FROM `homelike-bi-analysis.opportunity.__TABLES__`
```

You could get a list of all the tables and their
1. creation_time
2. last_modified_time
3. row_count
4. size_bytes
5. type


Alternatively, you could get some information through

```SQL
SELECT
 * EXCEPT(is_typed)
FROM
  `your_awesome_project.your_cool_dataset.INFORMATION_SCHEMA.TABLES`
```


These two queries return slightly different results.
