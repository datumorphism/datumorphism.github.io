---
title: "Jargons"
excerpt: "Jargons in statistics, accuracy, precision, population, sample, etl"
date: 2018-11-24
toc: true
category:
- 'Statistics'
tag:
- 'Statistics'
- 'Basics'
references:
- name: "Elements of Statistics by Stephen Bernstein and Ruth Bernstein"
  title: ''
weight: 1
---

## Accuracy and Precision

1. Accuracy: the measurement compared to the truth
2. Precision: variability of repeated measurements; the more precise, the less variations during each measurement.

| | Accurate | Inaccurate |
| Precise |  Close to true value, small variations in each measurement | Far from true value, small variations in each measurement  |
| Imprecise |  Close to true value, large variations in each measurement  |  Far from true value, large variations in each measurement  |

## Population and Sample

Physical Population and Measurement Population

1. Physical population: all the physical objects that satisfies the constraints of the measurement
2. Measurement population: the specified property of the physical population that is to be measured

Finite and Infinite

1. Finite population: finite number of elements in the population, such as the measurement of 11 football players in a match
2. Infinite population: infinite number of elements in the population, such as the 'size' of the stars in the universe through all time
3. Hypothetical population: if the infinite population doesn't really exist

Sample 

1. Physical sample: subset of physical population
2. Measurement sample: measurement of the physical sample

| | Population | Sample |
| Physical | physical objects | physical subset of the physical population |
| Measurement | measurement of the physical population |  measurement of the physical sample  |


## Hypothesis

1. Statistical hypothesis: hyposthesis about the measurement population
2. Research hypothesis or scientific hypothesis or working hypothesis: hypothesis about the physical population


## Loss Functions

1. RSS: residual sum-of-squares: $(\mathbf Y - \hat{\mathbf Y})^T(\mathbf Y - \hat{\mathbf Y})$ where $\mathbf Y$ is the actual data and $\hat{\mathbf Y}$ is the prediction