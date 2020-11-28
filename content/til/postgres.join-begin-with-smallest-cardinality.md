---
title: "Postgres Optimization in JOIN"
summary: "Join tables together starting with the smallest table (table with less cardinality) speeds things up."
date: 2020-11-28T11:39:21+01:00
authors:
  - Lei Ma
categories:
  - "data"
tags:
  - "Postgres"
  - "Warehouse"
---


To save resources, join tables together starting with the table with smallest cardinality whenever possible. Use `EXPLAIN` to understand the resource consumption in a query.