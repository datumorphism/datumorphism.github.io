---
title: Deal with NULL in Postgres
date: 2020-11-26
authors:
  - Lei Ma
categories:
  - data
tags:
  - Data Warehouse
  - Postgres
  - PGSQL
summary: "Please deal with null carefully."
---

`SUM` up some values with `NULL` in it, we get a value.

```
WITH base AS (
    SELECT
        1 AS num
    UNION ALL
    SELECT
        2 AS num
    UNION ALL
    SELECT
        NULL AS num
)
SELECT
    SUM(num)
FROM
    base
```

gives us

```
3
```

However, if one would add some values up, we get a NULL when one of them is `NULL`.

```
SELECT
NULL + 10 AS null_plus_num
```

gives us a

```
NULL
```

