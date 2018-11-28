---
title: "Some Concepts about Data Warehouse"
excerpt: ""
date: 2018-11-23
toc: true
category:
- 'Data Warehouse'
tag:
- 'Data Warehouse'
references:
- name: "Data Mining by Jiawei Han, Micheline Kamber, Jian Pei"
  link: ''
weight: 1
---

## The Three Key Ideas about Warehouse

The purpose of the data warehouse should be clear. In most cases, it is for the analysis of data, not for data production.[^1]

1. Subject-oriented: since data warehouses are for decision makers, arrange them into subjects makes it much easier to access.
2. Integraded: many sources are integrated for easy analysis
3. Time-variant: observation time should be recorded since the data is also used to analyze time evolution
4. Nonvolatile: simply for analysis


## OLTP and OLAP

1. OLTP: online transaction processing
2. OLAP: online analytical processing

|      | OLTP |  OLAP |
| user |    customer  |   data scientist, managers   |
| purpose | production | analysis  |
| content | everything | cleaner data |
| database | entity relation model, application oriented | star/snowflake model, subject oriented |
| history | usually no need to record the history | history is crucial |
| query | short and frequent read and write | read-only and but complicated analysis |


## Scope of Data Warehouse

1. Enterprise warehouse: targeting the whole organization
2. Data mart: for a specific group of people
3. Virtual warehouse: views not tables



[^1]: In fact, this is not always the case. Sometimes, data products can be delivered using some assist of data warehouse if the data product doesn't rely on the performance of the data source.