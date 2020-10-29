---
title: "OLAP Operations"
description: "Some useful OLAP operations"
date: 2018-11-23
category:
- 'Data Warehouse'
tags:
- 'OLAP'
references:
- name: "Data Mining, Section 4.2.5, by Jiawei Han, Micheline Kamber, Jian Pei"
  link: ''
weight: 3
---



## Roll-up or Drill-up

The word 'up' in the names refers to going up in concept hierarchies.

For example, we would like to know the revenue of the whole year. However, the record of data is

| Date | Revenue |
|---|---|
| 2018-01-01 | 1023 |
| 2018-01-02 | 934 |
| ... | ... |
| 2018-12-30 | 1244 |
| 2018-12-31 | 1302 |

Roll-up is performed by summing up everything of the column revenue. It gives us the revenue of the whole year. Monthly and quarterly roll-up is also straightforward.






