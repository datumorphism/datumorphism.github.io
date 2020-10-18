---
title: "Confusion Matrix (Contingency Table)"
excerpt: "Again, just like in hypothesis testing, we/machines all make mistakes. The question is, what kind of mistakes."
date: 2019-05-31
toc: true
category:
- 'Machine Learning::Basics'
tag:
- 'Statistical Learning'
- 'Basics'
- 'Learning Metrics'
- 'Classification'
references:
- name: 'Fawcett, T. (2006). An introduction to ROC analysis. Pattern Recognition Letters, 27(8), 861–874.'
  link: 'https://doi.org/10.1016/j.patrec.2005.10.010'
- name: 'Confusion_matrix#Table_of_confusion @ Wikipedia'
  link: 'https://en.wikipedia.org/wiki/Confusion_matrix#Table_of_confusion'
- name: 'F1 Score'
  link: 'https://en.wikipedia.org/wiki/F1_score'
weight: 1
---

* ToC
{:toc}

## Confusion Matrix

It is much easier to understand the confusion matrix if we use a binary classification problem as an example. For example, we have a bunch of cat photos and the user labeled "cute or not" data. Now we are using the labeled data to train a cute-or-not binary classifier.

Then we apply the classifier on the test dataset and we would only find four different kinds of results.

<table class="table">
  <thead>
    <tr>
      <th></th>
      <th>Labeled as Cute</th>
      <th>Labeled as Not Cute</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Classifier Predicted to be Cute</th>
      <td>True Positive (TP)</td>
      <td>False Positive (FP)</td>
    </tr>
    <tr>
      <th>Classifier Predicted to be Not Cute</th>
      <td>False Negative (FN)</td>
      <td>True Negative (TN)</td>
    </tr>
  </tbody>
</table>

This table is easy enough to comprehend. We have discussed the Type I and Type II errors in [Types of Errors in Statistical Hypothesis Testing
](/wiki/statistical-hypothesis-testing/type-1-error-and-type-2-error/). here False Positive (FP) is Type I error and False Negative (FN) is Type II error.

<div class="card">
	<header class="card-header">
		<p class="card-header-title card-toggle">Isn't FN type I error?</p>
	</header>
	<div class="card-content is-hidden">
		<div class="content">
			A first look at the table might lead us to conclude such as "FN is type I error" and "FP is type II error".

			But remember types of errors is about hypothesis testing and we usually test our null hypothesis. Here a null hypothesis is the negative labels.
		</div>
	</div>
</div>

Then we loop through all cats in the test dataset, find the results and put the numbers in the table.

There are a few things to look at whenever we have a table. First things first, we would like to know the sum of each row and columns.

1. The sum of the row "Classifier Predicted to be Cute" tells us the total number of cats classified as cute, aka, **Total Predicted Positives** (**PP**);
2. The sum of the row "Classifier Predicted to be Not Cute" tells us the total number of cats classified as not cute, aka, **Total Predicted Negatives** (**PN**);
3. The sum of the column "Labeled as Cute" tells us the total number of cats labeled as cute in the test dataset, aka, **Total Positives** (**P**);
4. The sum of the column "Labeled as Not Cute" tells us the total number of cats labeled as not cute in the test dataset, aka, **Total Negatives** (**N**).
5. The sum of the diagonal elements tells us the total number of cases where the classifier classified the data correctly.

## Measures Defined

### Property of the Dataset itself

Apart from these trivial properties about the test dataset defined above, we can define the **Prevalence**:

$$
\frac{ \text{ Total Positives } }{ \text{ Total Sample, or Total Positives + Total Negatives} } = \frac{ \text{ Labeled as Cute } }{ \text{ All Cats, or Labeled as Cute + Labeled as Not Cute} }
$$

### Performance of Classifier

We could define some quite general measures.

1. **Accuracy**:
  $$\frac{ \text{ TP + TN } }{ \text{P + N} }$$

Now we recalculate the confusion matrix by dividing the values by some certain sums.


#### Confusion Matrix divided by the Column Sums

As mentioned in the previous sections, the sum of the columns are **P** (**Total Positives**) and **N** (**Total Negatives**). Dividing each column by the sum of the corresponding column gives us the prediction rate for each labels.

<table class="table">
  <thead>
    <tr>
      <th></th>
      <th>Labeled as Cute</th>
      <th>Labeled as Not Cute</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Classifier Predicted to be Cute</th>
      <td>True Positive Rate (aka Recall) = TP/P</td>
      <td>False Positive Rate = FP/N</td>
    </tr>
    <tr>
      <th>Classifier Predicted to be Not Cute</th>
      <td>False Negative Rate = FN/P</td>
      <td>True Negative Rate (aka Specifity) = TN/N</td>
    </tr>
  </tbody>
</table>


There are a few names to be emphasized.

1. **Recall**: True Positive Rate

#### Confusion Matrix divided by the Row Sums

As mentioned, the sum of the rows indicates the

<table class="table">
  <thead>
    <tr>
      <th></th>
      <th>Labeled as Cute</th>
      <th>Labeled as Not Cute</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Classifier Predicted to be Cute</th>
      <td>Positive Predictive Value (aka Precision) = TP/PP</td>
      <td>False Discovery Rate = FP/PP</td>
    </tr>
    <tr>
      <th>Classifier Predicted to be Not Cute</th>
      <td>False Omission Rate = FN/PN</td>
      <td>Negative Predictive Value = TN/PN</td>
    </tr>
  </tbody>
</table>

There are a few names to be emphasized.

1. **Precision**: Positive Predictive Value

#### Ratios, Scores, and More


We also have some other definitions of ratios, please refer to the bottom left corner of the table on the wikipedia page linked in the references.

We will only define the F1 score ($\mathrm F_1$) here. As a F-measure,

$$
\begin{align}
F_1 &= \frac{2}{ 1/\mathrm{Pression} + 1/\mathrm{Recall} } \\
& = \frac{2}{ \frac{PP}{TP} + \frac{P}{TP} } \\
& = \frac{2}{ \frac{PP+P}{TP} } \\
& = \frac{2}{ \frac{ (TP + FP) + (TP + FN) }{TP} } \\
& = \frac{1}{ 1 + \frac{ (FP + FN) }{2TP} }
\end{align}
$$

## Confused by the Names?

There is a nice chart on [this wikipedia page](https://commons.wikimedia.org/wiki/File:Precisionrecall.svg).

The different metrics can be visualized using color blocks. We use green to represent the amount of TP, orange to represent the amount of FP.

<figure markdown="1">
![](../confusion-matrix/confusion-matrix-less-tp-more-fp.png)
<figcaption markdown="1">
Low TP Rate;High FP Rate; Low Precision; Low Accuracy; Low Recall; Low F1
</figcaption>
</figure>

<figure markdown="1">
![](../confusion-matrix/confusion-matrix-more-tp-more-fp.png)
<figcaption markdown="1">
High TP Rate;High FP Rate; Not so good Precision; Not so good Accuracy; High Recall; Not so good F1
</figcaption>
</figure>


<figure markdown="1">
![](../confusion-matrix/confusion-matrix-more-tp-less-fp.png)
<figcaption markdown="1">
High TP Rate;Low FP Rate; Good Precision; Good Accuracy; High Recall; Good F1
</figcaption>
</figure>

<figure markdown="1">
![](../confusion-matrix/confusion-matrix-less-tp-less-fp.png)
<figcaption markdown="1">
Low TP Rate;Low FP Rate; Low Precision; Low Accuracy; Low Recall; Low F1
</figcaption>
</figure>

<figure markdown="1">
![](../confusion-matrix/confusion-matrix-less-tp-lesser-fp.png)
<figcaption markdown="1">
Low TP Rate;Low FP Rate; High Precision; Low Accuracy; Low Recall; Low F1
</figcaption>
</figure>








