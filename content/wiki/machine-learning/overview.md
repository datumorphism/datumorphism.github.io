---
title: "Machine Learning Overview"
description: "A brief overview of machine learning"
date: 2018-05-25
categories:
- 'Machine Learning'
tags:
- 'Statistical Learning'
- 'Machine Learning'
- 'Basics'
weight: 1
references:
  - name: "Mehta, P., Bukov, M., Wang, C. H., Day, A. G. R., Richardson, C., Fisher, C. K., & Schwab, D. J. (2019). A high-bias, low-variance introduction to Machine Learning for physicists. Physics Reports, 810, 1–124."
    link: "https://doi.org/10.1016/j.physrep.2019.03.001"
  - name: "Shalev-Shwartz, S., & Ben-David, S. (2013). Understanding machine learning: From theory to algorithms. Understanding Machine Learning: From Theory to Algorithms"
    link: "https://doi.org/10.1017/CBO9781107298019"
  - name: "Domingos, P. (2012). A few useful things to know about machine learning. Communications of the ACM, 55 (10), 78–87."
    link: "https://doi.org/10.1145/2347736.2347755"
    key: "Domingos2012"
  - name: "Abu-Mostafa, Yaser S and Magdon-Ismail, Malik and Lin, Hsuan-Tien. Learning from Data. 2012. Available: https://www.semanticscholar.org/paper/Learning-From-Data-Abu-Mostafa-Magdon-Ismail/1c0ed9ed3201ef381cc392fc3ca91cae6ecfc698"
    link: "https://www.semanticscholar.org/paper/Learning-From-Data-Abu-Mostafa-Magdon-Ismail/1c0ed9ed3201ef381cc392fc3ca91cae6ecfc698"
    key: "Abu-Mostafa2012"
  - name: "Deckert D-A. Advanced Topics in Machine Learning. In: Advanced Topics in Machine Learning [Internet]. Apr 2017 [cited 17 Oct 2021]. Available: https://www.mathematik.uni-muenchen.de/~deckert/teaching/SS17/ATML/"
    link: "https://www.mathematik.uni-muenchen.de/~deckert/teaching/SS17/ATML/"
    key: "Deckert2017"
links:
  - cards/machine-learning/learning-theories/learning-problem.md
  - wiki/learning-theory/vc-dimension.md
---


## What is Machine Learning

Abu-Mostafa, Magdon-Ismail, and Lin summarized machine learning problem using the following chart [^Abu-Mostafa2012] [^Deckert2017]. Utilimately, we need to find an approximation $g$ of the true map $f$ from features $\mathcal X$ to targets $\mathcal Y$ on a specific probability distribution of features $P$. This process is done by using an algorithm to select some hypothesis that works.

{{< figure src="../assets/overview/abu-mostafa-magdon-lin-ml-framework.png" caption="From the book *Learning From Data* by Abu-Mostafa, Magdon-Ismail, and Lin. I am using a version by Deckert." >}}


In the core of machine learning models, we have three components[^Domingos2012]:

- Representation: encode data and problem representation, i.e., propose a space to set a stage.
- Evaluation: an objective function to be evaluated that guides the model.
- Optimization: an algorithm to optimize the model so it learns what we want it to do.


{{< figure src="../assets/overview/three-components-of-learning-algorithms.png" caption="Table from Domingos2012" >}}






## Machine Learning Workflow

There are many objectives in machine learning. Two of the most applied objectives are classifications and regressions. In classifications and regression, the following four factors are relevant.

{{< figure src="../assets/overview/machine-learning-framework.png" caption="A simple framework of machine learning. The dataset $\tilde{\mathscr D}$ is first encoded by $\mathscr T$, $\mathscr D(\mathbf X, \mathbf Y) = \mathscr T(\tilde{\mathscr D})$. The dataset is feeded into the model, $\bar{\mathbf Y} = f(\mathbf X;\mathbf \theta)$. The model is then tested with the test method, $L_{f, \mathscr D}(h)$. By requiring the test method to satisfy some specific conditions, we solve the model parameters $\mathbf\theta$." >}}


1. Input:
   1. Domain knowledge $\tilde{\mathscr K_D}$.
      1. on features,
      2. on target values,
      3. on relation between features and target values.
   2. A dataset $\tilde{\mathscr D}(\tilde{\mathbf X}, \tilde{\mathbf Y})$ with $\tilde{\mathbf X}$ being the features and $\tilde{\mathbf Y}$ being the values to be predicted;
      1. features (domain set): $\tilde{\mathbf X}$,
      2. target values (label set): $\tilde{\mathbf Y}$.
      3. relations between features and target values: $f(\mathbf X) \to \mathbf Y$.
2. A set of "encoders" $\mathscr T_i$ that maps the features $\tilde{\mathbf X}$ into machine-readable new features $\mathbf X$ and predicting values $\tilde{\mathbf y}$ into machine readable new values $\mathbf y$. The dimensions of $\tilde{\mathbf X}$ and $\mathbf X$ may not be the same. In summary, $\mathscr T(\tilde{\mathscr D}) \to \mathscr D$.
3. A model (aka, prediction rule, predictor, hypothesis) $h(\mathbf X;\mathbf \theta)\to \bar{\mathbf Y}$ that maps $\mathbf X$ to the values with $\mathbf X$ being a set of input features. $h$ may also be a set of functions.
4. A measurement of the model performance, $L_{f, \mathscr D}(h)$.
   1. Error of model: $L_{f, \mathscr D}(h) = \mathscr L(h(\mathbf X), f(\mathbf X))$, where $\mathscr L$ is distance operator.



[^Domingos2012]: {{< cite key="Domingos2012" >}}
[^Abu-Mostafa2012]: {{< cite key="Abu-Mostafa2012" >}}
[^Deckert2017]: {{< cite key="Deckert2017" >}}