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

#### Python

Some essential libraries:

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

Use virtual environments:
- virtualenv
- conda
  - {{< c "tags/anaconda/" "Articles with Anaconda tag" >}}

Use notebooks
- Jupyter
  - {{< c "tags/jupyter" "Articles with Jupyter tag" >}}



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
- Regular Expression
  - {{< c "wiki/sugar/regular-experssions.md" >}}
- Scraping
  - {{< c "wiki/nodecrawler" >}}
  - {{< c "tags/web-scraping/" "Articles tagged Web Scraping">}}


## Statistics


### Descriptive statistics

> It is crucial for the interpretations in statistics.

- Probability theory
  - random variable
  - probability distribution
    - pdf
    - pmf
    - {{< c "tags/distributions/" "articles tagged with distributions">}}
  - Bayes
    - {{< c "tags/bayesian/" "Articles with tagged with Bayesian">}}
- Summary statistics
  - location
  - variation
  - correlation
    - {{< c "cards/statistics/covariance-matrix.md" >}}
    - {{< c "cards/statistics/explained-variation.md" >}}
    - {{< c "wiki/statistics/correlation-coefficient.md" >}}
- Laws
  - Law of large numbers
  - Central limit theorem
  - Law of total variance
  - much more
- Probability Estimation
  - Kernel density estimation




### Inferential statistics

> To get closer to the ultimate question about causality

- Parameter Estimation
  - Maximum Likelihood
- Hypothesis Testing
  - {{< c "wiki/statistical-hypothesis-testing" >}}
- Inference
  - Bayesian inference
    - Confidence interval
    - {{< c "tags/bayesian/" "Articles with tagged with Bayesian">}}
  - Frequentist inference

## EDA

Data wrangling and exploratory data analysis.

### Understand the Source of the data

- Know the source
- Understand the data collection procedure
- Understand the limitation of the data

### Dimensionality and Numerosity Reduction

Reduce the dimension of the data:
- PCA
  - {{< c "wiki/machine-learning/unsupervised/pca.md" >}}
- SparsePCA
- ICA

Numerosity reduction:
- Parametric
  - Using model parameters to represent the data
- Non-parametric
  - Histograms
  - Clustering
  - Resampling


### Data Normalization

Normalization is very important in many models.

Normalization of raw data:
- {{< c "wiki/statistics/normalization-methods.md">}}

Normalization in neural networks:
- Batch normalization

### Missing Data

Data imputation

### Unbiased Estimators


### Binning

- Bin the sparse values
- Bin continuous data if necessary


### Outlier Detection


### Anomaly Detection


### Noisy Data

### Sampling and Resampling

### Feature Selection


### Baseline Model

#### Association Rules


## Visualization

### What to show

- Relationship
- Composition
  - Compose to compare
  - Compose to calculate (the total)
  - Compose to form a distribution


### Types of Charts


{{< figure src="assets/choosing-a-good-chart-09.png" caption="Know your charts. Source: [Chart Suggestions — A Thought-Starter](https://extremepresentation.typepad.com/files/choosing-a-good-chart-09.pdf)" >}}



### Grammar of Graphics

- {{< c "reading/grammar-of-graphics/graph-creation.md" >}}
- {{< c "reading/grammar-of-graphics" >}}

### Tools

- Python
  - matplotlib
    - {{< c "tags/matplotlib/" "articles tagged with matplotlib" >}}
  - seaborn
  - plotnine
  - plotly
- Dashboarding
  - streamlit
  - plotly dash

## Machine Learning

### Concepts

- Features
- Estimators
- Risk
  - {{< c "cards/machine-learning/learning-theories/empirical-risk-minimization.md" >}}
  - {{< c "cards/machine-learning/learning-theories/structural-risk-minimization.md" >}}
  - {{< c "cards/machine-learning/learning-theories/cross-validation.md" >}}
- Bias and Variance
- Overfitting, Underfitting
  - {{< c "wiki/model-selection/goodness-of-fit.md" >}}
- Performance
  - Regression
    - R^2
  - Classification
    - F score
    - Precision
    - Recall


### Frameworks

#### Supervised


##### Regression

- Linear Regression
- Higher-order Regression


##### Classification

- Logistic Regression
- SVM
- Tree


#### Unsupervised



#### Semi-supervised

#### Reinforcement Learning






## Graphs and Networks

## Neural Networks





[^Kretz2019]: {{< cite key="Kretz2019" >}}