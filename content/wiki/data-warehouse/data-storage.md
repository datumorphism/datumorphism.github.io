---
title: "Data Storage"
date: 2018-11-23
categories:
- 'Data Warehouse'
tags:
- 'Data Warehouse'
weight: 4
---


`tl;dr`: Use type safe formats such as HDF5 or parquet

1. HDF5
2. `BCOLZ <http://bcolz.blosc.org/en/latest/>`_ : not designed for multidimentional data.
3. `Zarr <https://github.com/alimanfoo/zarr>`_ : works with multidimensional data and also parallel computating.
4. `Blaze ecosystem <http://blaze.pydata.org/>`_

A article that compares HDF5, BCOLZ, and Zarr: [To HDF5 and beyond](http://alimanfoo.github.io/2016/04/14/to-hdf5-and-beyond.html)

I also recommend pandas. It is a python module that works very well with data. It even loads HDF5 out of box.
