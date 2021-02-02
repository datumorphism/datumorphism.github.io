---
title: "Postgres Optimization in JOIN"
summary: "Join tables together starting with the smallest table (table with less cardinality) speeds things up."
date: 2020-11-28T11:39:21+01:00
authors:
  - Lei Ma
categories:
  - "data"
references:
  - name: "Postgres Explain Visualizer 2"
    link: "https://explain.dalibo.com/"
  - name: "Using EXPLAIN @ Postgres documentation"
    link: "https://www.postgresql.org/docs/9.4/using-explain.html"
tags:
  - "Postgres"
  - "Warehouse"
---


To save resources, one should join tables together starting from the one that has the smallest cardinality whenever possible.

To inspect the cost of the query, append `EXPLAIN` to the query so that we can get an execution plan.

One could visualize the `EXPLAIN` results using visualizers such as [this one](https://explain.dalibo.com/) [by dalibo](https://github.com/dalibo/pev2).

