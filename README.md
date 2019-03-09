[![Build Status](https://travis-ci.org/UBC-MDS/pyfer.svg?branch=master)](https://travis-ci.org/UBC-MDS/pyfer)

# Pyfer

Pyfer provides a tidy way of performing statistical inference built on top of Pandas.

|Name |Github |
|-|-|
|Gabriel Bogo|[@GabrielBogo](https://github.com/GabrielBogo)|
|Yuwei Liu |[@liuyuwei169](https://github.com/liuyuwei169)|
|Weifeng Davy Guo |[@DavyGuo](https://github.com/DavyGuo)|
|Mohamad Makkaoui |[@makka3](https://github.com/makka3)|


The `infer` package in R utilizes functions that are built with the emphasis on clear expressive code and using correct statistical grammar to perform statistical inference.

With that package as the inspiration, `pyfer` will have four main functions (`specify`,`generate`,`calculate`,`get_ci`) for the first iteration. These functions will streamline the process of reshuffling and bootstrapping of samples, compiling summary statistics, and calculating confidence intervals.

Currently, there isn't a package in Python's ecosystem that does a great job at replicating the `infer` package's functionality, easy-of-use, and use of expressive statistical grammar. Pyfer fills that gap and provides the basic tools to perform statistical inference in Python.

## Installing `pyfer`

To install using pip, on your command line type:

`pip install git+https://github.com/UBC-MDS/pyfer.git`

## Usage example (with Pandas)

```
import pandas as pd
import pyfer

#Loading a sample dataset in Pandas
mpg = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv')

mpg_acc = pyfer.specify(mpg, response="acceleration")
mpg_resampled = pyfer.generate(mpg_acc, n_samples=30, type="bootstrap")
mpg_mean = pyfer.calculate(mpg_resampled, columns="acceleration", stat="mean")
mpg_ci = pyfer.get_ci(mpg_mean,level=0.9, point_estimate=None)
```

## Branch Coverage

Because of the time limit, we were not able to get a 100% branch coverage. However, we get one that is very close. Here are the links for our screenshot:

[screenshot1](https://github.com/UBC-MDS/pyfer/blob/img/img/coverage.png)

[screenshot2](https://github.com/UBC-MDS/pyfer/blob/img/img/coverage2.png)
