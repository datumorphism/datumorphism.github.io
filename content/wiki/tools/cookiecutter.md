---
title: "Cookiecutter"
description: "Use cookiecutter to initialize a project"
date: 2021-08-27
categories:
    - 'Tools'
tags:
    - 'Tools'
    - 'Python'
    - 'Data Science'
references:
  - name: 'drivendata. drivendata/cookiecutter-data-science: A logical, reasonably standardized, but flexible project structure for doing and sharing data science work. In: GitHub [Internet]. [cited 27 Aug 2021]. Available: https://github.com/drivendata/cookiecutter-data-science'
    link: "https://github.com/drivendata/cookiecutter-data-science"
  - name: "cookiecutter. cookiecutter/cookiecutter: A command-line utility that creates projects from cookiecutters (project templates), e.g. Python package projects, VueJS projects. In: GitHub [Internet]. [cited 27 Aug 2021]. Available: https://github.com/cookiecutter/cookiecutter"
    link: "https://github.com/cookiecutter/cookiecutter"
links:
  - "wiki/tools/documentation.md"
  - "wiki/programming-languages/python/_index.md"
weight: 7
---

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) is a good tool to setup a scaffold for a data science project. [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science) is a very good template to use.

If some specific (internal) packages are needed for almost every package, fork [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science) and make some changes for future use. For example, one might use {{< c "wiki/tools/documentation.md" "mkdocs" >}} instead of {{< c "wiki/tools/documentation.md" "sphinx" >}}. Swap out sphinx for mkdocs if needed.
