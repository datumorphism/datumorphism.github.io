---
title: "Documentation"
description: "Documenting my data science project using sphinx or mkdocs-material"
date: "2021-08-28T00:03:10+02:00"
categories:
    - "Tools"
tags:
    - "Tools"
    - "Python"
    - "Documentation"
references:
  - name: "sphinx-doc. sphinx-doc/sphinx: Main repository for the Sphinx documentation builder. In: GitHub [Internet]. [cited 28 Aug 2021]. Available: https://github.com/sphinx-doc/sphinx"
    link: "https://github.com/sphinx-doc/sphinx"
    key: "sphinx"
  - name: "Read the Docs"
    link: "https://readthedocs.org/"
    key: "rtd"
  - name: "squidfunk. squidfunk/mkdocs-material: Technical documentation that just works. In: GitHub [Internet]. [cited 28 Aug 2021]. Available: https://github.com/squidfunk/mkdocs-material"
    link: "https://squidfunk.github.io/mkdocs-material/"
    key: "mdm"
weight: 8
---

I would vote for two very different documentation tools for a data science project,

- [sphinx docs](https://github.com/sphinx-doc/sphinx), and
- [squidfunk/mkdocs-material](https://squidfunk.github.io/mkdocs-material/).


## Sphinx docs

Sphinx docs is a mature and stable. I love [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) as the syntax as it is very versatile. It supports math, figures with captions, admonitions, cross reference, auto doc from docstrings, cross project cross referencing, pdf generation, etc.

{{< message title="reStructuredText is not the only choice" class="info" >}}
We can also use markdown by [choosing the markdown parser](https://www.sphinx-doc.org/en/master/usage/markdown.html).
{{< /message >}}



## squidfunk/mkdocs-material

squidfunk's mkdocs-material is a rather light-weight but is also growing to be versatile now. The engine is mkdocs. mkdocs-material is a theme but provides a lot of useful and easy to use elements.

The package ships a lot of plugins and extensions for documentation. We can generate docs from docstrings, write admonitions, write math, etc. We can also install plugins to extend the functions, e.g., [pdf generation](https://github.com/orzih/mkdocs-with-pdf).

One more thing, mkdocs-material is prettier than most sphinx docs themes.

## Which on to use

If you have never used sphinx, I recommend starting from mkdocs-material. But it is really just a personal taste.

Roll a dice.