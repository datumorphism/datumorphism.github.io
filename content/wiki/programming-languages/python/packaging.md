---
title: "The Python Language: Packaging"
description: "Build a python package"
date: "2021-08-27"
categories:
  - "Programming Language"
tags:
  - "Python"
  - "Programming Language"
  - "Basics"
references:
  - name: "Torborg S. How To Package Your Python Code — Python Packaging Tutorial."
    link: "https://python-packaging.readthedocs.io/en/latest/index.html"
    key: "Torborg2016"
  - name: "Python Packaging User Guide — Python Packaging User Guide."
    link: "https://packaging.python.org/"
    key: "documentation"
links:
  - "wiki/programming-languages/python/_index.md"
weight: 5
---


The official documentation has pages about building python packages[^documentation]. Torborg also compiled a series of pages and examples about building a package[^Torborg2016]. In this note, I only provide some tips.


## Private Python Packages

We can easily setup a private pypi service (e.g., [pypicloud](https://pypicloud.readthedocs.io)).


### Install Packages from Private Pypi

To install packages inline, use

```
pip install -i https://$PYPI_USER:$PYPI_PWD@your.pypi.url/simple/ durst==0.0.5
```

To install packages from `requirements.txt` use,

```
pip install -r requirements.txt --trusted-host https://$PYPI_USER:$PYPI_PWD@your.pypi.url/simple --extra-index-url https://$PYPI_USER:$PYPI_PWD@your.pypi.url/simple
```

## Publishing Packages Using GitHub Actions

We can easily publish python packages using GitHub Actions. Here is an example.

```yaml
name: Publish Package to Private Pypi

on: [push]

jobs:
  build-n-publish:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.7
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install -r requirements-dev.txt
      - name: Generate dist
        run: python setup.py sdist
      - name: Publish package
        if: github.event_name == 'push' && startsWith(github.ref, 'refs/tags')
        uses: pypa/gh-action-pypi-publish@master
        with:
          user: ${{ secrets.private_pypi_username }}
          password: ${{ secrets.private_pypi_password }}
          repository_url: ${{ secrets.private_pypi_url }}
```



## Test Python Packages Using GitHub Actions

Continuous testing packages before publishing is crucial for the stability of the packages.


```yaml
name: Test Code with Pip

on: [push]

jobs:
  build:
    strategy:
      matrix:
        python-version: [3.6, 3.7, 3.8]
        os: [ubuntu-latest, macos-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install -r requirements-dev.txt
          # install black if available (Python 3.6 and above), and autopep8 for testing the pipe mode
          pip install black || true
          pip install autopep8 || true
      - name: Lint with flake8
        run: |
          # stop the build if there are Python syntax errors or undefined names
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
          # all Python files should follow PEP8
          # echo "flake8 all python"
          # flake8 durst tests
          # exit-zero treats all errors as warnings.  The GitHub editor is 127 chars wide
          echo "flake8 BLK"
          flake8 durst --count --exit-zero --max-complexity=18 --statistics --select BLK
      - name: Install from source (required for the pre-commit tests)
        run: pip install .
      - name: Test with pytest
        run: pytest --cov=durst -W ignore::DeprecationWarning
```



## Build Documentation Using GitHub Actions

The following configuration builds the documentation using sphinx and deploys the content to S3.

```yaml
name: Test Build Docs

on:
  push:
    branches:
      - "**"
      - "!gh-pages"

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        with:
          submodules: true  # Fetch Hugo themes
          fetch-depth: 0    # Fetch all history for .GitInfo and .Lastmod

      - uses: ammaraskar/sphinx-action@master
        with:
          docs-folder: "docs/"

      - uses: actions/upload-artifact@v1
        with:
          name: DocumentationHTML
          path: docs/build/html/

      - name: Deploy to S3
        uses: jakejarvis/s3-sync-action@master
        with:
          args: --delete
        env:
          AWS_S3_BUCKET: ${{ secrets.AWS_S3_BUCKET }}
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          AWS_REGION: ${{ secrets.AWS_REGION }}
          SOURCE_DIR: 'public'
```

Building docs using mkdocs is similar. Here is a minimal example.

```yaml
name: Publish Docs
on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.x
      - run: pip install mkdocs
      - run: pip install mkdocs-material
      - run: pip install mkdocs-material-extensions
      - run: pip install mkdocs-autorefs
      - run: pip install mkdocstrings
      - run: pip install -e ".[all]"
      - run: mkdocs gh-deploy --force
```




[^documentation]: {{< cite key="documentation" >}}
[^Torborg2016]: {{< cite key="Torborg2016" >}}
