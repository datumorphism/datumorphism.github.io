---
layout: til
title: "Get Current User in BigQuery"
date: 2019-05-12
author: Lei Ma
comments: true
category:
- data
tag:
- Data Warehouse
- Big Query
excerpt: BigQuery Current User
---

You could get the current user id in BigQuery.

```SQL
SELECT SESSION_USER() as user, GENERATE_UUID() AS uuid
```