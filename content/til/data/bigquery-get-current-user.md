---
title: "Get Current User in BigQuery"
date: 2019-05-12
authors:
  - Lei Ma
categories:
- data
tags:
- Data Warehouse
- Big Query
summary: BigQuery Current User
---

You could get the current user id in BigQuery.

```SQL
SELECT SESSION_USER() as user, GENERATE_UUID() AS uuid
```