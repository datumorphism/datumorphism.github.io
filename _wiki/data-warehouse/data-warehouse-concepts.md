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


## Fact and Dimension

**Fact** is the value of something specified by the **dimension**. For example, we have a table that tells us the revenue of the year 2018 for keyboards is 3 million euros. 

|  `Year` | `Category`  |  Revenue |
|--|---|---|
| 2017 | Keyboard | 2,500,000 |
| 2017 | Headset | 200,000 |
| 2018 | Keyboard | 3,000,000 |
| 2018 | Headset | 134,000  |

The columns `Year` and `Category` serve as dimensions and `Revenue` serves as the fact.

The dimension tells us what we are talking about and the fact tells us the values. For the previous example, we could set up a coordinate system, with two axes, `Year` and `Category`. On the `Year` axis, we have two values, `2017` and `2018`. On the `Category` axis, we have two values `Keyboard` and `Headset`. If we are looking for the revenue of keyboards in 2018, then we are looking for `2018` and `Headset`. It is clearly a 2 dimensional **data cube**.


In princple, we could have N dimensional **data cube**. For example, we would like to look at the revenue of 

1. keyboards (`Category`),
2. in 2018 (`Year`),
3. in Cologne (`City`),
4. sold offline (`Channel`).

Then we have a 4 dimensional dataset. Revenue is the fact and `Category`, `Year`, `City` and `Channel` are the dimensions.



## Concept Hierarchies

Concept hierarchies are crucial to OLAP operations. 

We consider a data cube about revenue with the dimension `Date` with values such as 2018-11-26. We would like to know the monthly revenue, the quarterly revenue, and the annual revenue. It's straightforward to calculate those. The idea is that monthly, quarterly, and annual revenue form a hierarchy: day $\in$ month $\in$ quarter $\in$ year. This is a convention used by everyone on this planet.

In some other cases, concept hierarchies are very much designed instead of being a convention. Suppose we record the prices of houses. It would be nice to categorize the prices into different ranges of prices. Some would say, we divide them into five ranges:
1. below 25 percentile
2. 25 to 50 percentile
3. 50 to 75 percentile
4. above 75 percentile

Others would say, we divide them into 100 euros segments
1. 0 to 100 euros
2. 100 to 200 euros
3. ...






 













[^1]: In fact, this is not always the case. Sometimes, data products can be delivered using some assist of data warehouse if the data product doesn't rely on the performance of the data source.