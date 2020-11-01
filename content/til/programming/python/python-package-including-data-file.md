---
layout: til
title: "Add Data Files to Python Package"
date: 2019-03-13
author: Lei Ma
category:
- programming
- basics
tags:
- Python
references:
  - name: Including non-Python files with setup.py
    link: https://stackoverflow.com/Questions/1612733/including-non-python-files-with-setup-py
excerpt: Add Data Files to Python Package using manifest.in and setup.py
---

Suppose we have a file `auth.json` for some credentials for the package.

First of all, include this file in your `MANIFEST.in`

```
include hl_42/config/auth.json
```

To make it work, we have to enable `include_package_data` in `setup.py`. For example, we could write the setup function like this:

```
from setuptools import setup as _setup

def setup():
    _setup(name = PACKAGE_NAME,
      version = PACKAGE_VERSION,
      description = PACKAGE_DESCRIPTION,
      long_description = PACKAGE_LONG_DESCRIPTION,
      url = PACKAGE_URL,
      author = 'Lei Ma',
      author_email = 'lei.ma@homelike.cc',
      license = 'MIT',
      packages = _find_packages(exclude=('tests',)),
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
```

