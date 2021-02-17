---
title: "Coding Theory Concepts"
date: 2021-02-17
category:
  - 'Information'
tags:
  - Information Theory
  - Entropy
references:
  - link: "https://mbernste.github.io/posts/sourcecoding/#:~:text=Shannon's%20Source%20Coding%20Theorem%20tells,to%20unambiguously%20communicate%20those%20samples.&text=In%20this%20post%2C%20we%20will%20walk%20through%20Shannon's%20theorem."
    name: "Shannon’s Source Coding Theorem (Foundations of information theory: Part 3)"
  - link: "http://www.cs.cmu.edu/~aarti/Class/10704/lec8-srccodingHuffman.pdf"
    name: "Lecture 8: Source Coding Theorem, Huffman coding by Aarti Singh"
  - link: "https://homepages.dcc.ufmg.br/~msalvim/courses/infotheory/L03_TheSourceCodingTheorem%5Bstill%5D.pdf"
    name: "The Source Coding Theorem by Mario S. Alvim"
---


![](../assets/coding-theory-concepts.png)

The code function produces code words. The expected length of the code word is limited by the entropy from the source probability $p$.

The Shannon information content, aka self-information, is described by

{{< m >}}
- \log_2 p(x=a),
{{< /m >}}

for the case that $x=a$.

The Shannon entropy is the expected information content for the whole sequence with probability distribution $p(x)$,

{{< m >}}
\mathcal H = - \sum_x p(x\in X) \log_2 p(x).
{{< /m >}}

The Shannon source coding theorem says that for $N$ samples from the source, we can *roughly* compress it into $N\mathcal H$.