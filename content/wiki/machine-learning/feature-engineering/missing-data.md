---
title: "Dealing with Missing Data in Machine Learning"
description: "During feature engineering, we have to deal with missing values."
date: 2019-08-05
authors:
  - "LM"
categories:
  - "Machine Learning"
tags:
  - "Machine Learning"
  - "Feature Engineering"
  - "Data"
weight:
links:
  - "wiki/machine-learning/feature-engineering/data-types.md"
  - "wiki/statistics/normalization-methods.md"
---



## How to Deal with Missing Data

1. Remove
	1. Listwise deletion: Remove the whole record; Works if the missing values are random.
	2. Removing values causes problem in many aspects. For example, we can not just delete data when applying our models.
2. Replace
   1. with most frequent value
   2. central tendency: median, mean, etc
   3. fixed value: a string etc
3. New Category: define a new category for missing data
4. Convert the column to a binary valued column indicating if the feature is missing or not.


## Tools

1. pandas
2. sklearn: Imputer
3. @ResidentMario/missingno : visualize missing data

