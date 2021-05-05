---
layout: page
title: Curriculum
description: The path that I follow
category:
  - 'Curriculum'
tags:
  - "roadmap"
  - "career"
references:
  - name: "The Data Engineering Cookbook"
    link: "https://github.com/andkret/Cookbook"
    key: "Kretz2019"
supplementary:
  - name: "AI Expert Roadmap"
    link: "https://i.am.ai/roadmap/#fundamentals"
  - name: "The Data Engineering Cookbook"
    link: "https://github.com/andkret/Cookbook"
exclude: true
links:
  - "wiki/data-engeering-for-data-scientist/checklist/"
---


## Prerequisites

### Programming

- Bash:
  - {{< c "tags/bash" "all posts with the bash tag" >}}
- Python:
  - {{< c "wiki/programming-languages/python" >}}
  - {{< c "tags/python" "all posts with the python tag" >}}
- C++:
  - {{< c "wiki/programming-languages/cpp" >}}
  - {{< c "tags/c++" "all posts with the C++ tag" >}}

alternatives:

- R
- Matlab

#### Python Libraries

- Data
  - numpy
  - scipy
  - pandas
  - dask
- Visualization
  - matplotlib
  - seaborn
  - plotly
- and your machine learning libraries


### Computer Science

> These theories make people think faster. They don't pose direct limits on what data scientists can do but they will definitely give data scientists a boost.

- {{< c "wiki/computation/basics-of-computation.md" >}}
- {{< c "wiki/algorithms/data-structure.md" >}}
  - {{< c "wiki/algorithms/data-structure-tree.md" >}}
  - {{< c "wiki/algorithms/data-structure-graph.md" >}}
- Algorithms
  - Complexity
  - [HackerRank](https://www.hackerrank.com/domains/algorithms)


### Math

> Some basic understanding of these is absolutely required. Higher levels of these topics will also be listed in details.

- Statistics
  - {{< c "cards/statistics/" "Statistics Concepts">}}
  - {{< c "wiki/statistics/" "Statistical Methods">}}
- Linear Algebra
  - {{< c "tags/linear-algebra/">}}
- Calculus
- Differential Equations
  - {{< c "tags/differential-equation/" >}}


## Engineering for Data Scientist

I use the book by Adreas Kretz as a checklist [^Kretz2019].

{{< c "wiki/data-engeering-for-data-scientist/checklist.md" >}}



## Data Storage and Retrieval

- Database Basics
  - {{< c "wiki/computation/basics-of-database.md" >}}
- Data Files
  - {{< c "cards/machine-learning/datatypes/data-file-formats.md" >}}
- Query Language
  - SQL
    - {{< c "wiki/computation/basics-of-sql.md">}}
    - {{< c "tags/sql" "SQL tag">}}
  - PGSQL
    - {{< c "tags/pgsql" "PGSQL tag">}}



## Statistics


### Descriptive statistics

> It is crucial for the interpretations in statistics.

### Inferential statistics

> To get closer to the ultimate question about causality

- Hypothesis Testing
- Bayesian inference
- Frequentist inference

## Visualization

### Types of Data

### Types of Charts

### Grammar of Graphics

## EDA

### Dimensionality Reduction


### Association Rules

### Anomaly Detection


## Statistical Learning

### Regression

- Linear Regression
- Higher-order Regression


### Classification

- Logistic Regression
- SVM
- Tree



## Graphs and Networks

## Natural Language Processing



[^Kretz2019]: {{< cite key="Kretz2019" >}}