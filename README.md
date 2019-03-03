# Pyfer


|Name |Github |
|-|-|
|Gabriel Bogo|[@GabrielBogo](https://github.com/GabrielBogo)|
|Yuwei Liu |[@liuyuwei169](https://github.com/liuyuwei169)|
|Weifeng Davy Guo |[@DavyGuo](https://github.com/DavyGuo)|
|Mohamad Makkaoui |[@makka3](https://github.com/makka3)|


Python implementation of the `infer` R package, that offers a tidy way of developing statistical inference built on top of Pandas.

The `infer` package in R streamlines the process of reshuffling and bootstrapping of samples, calculating summary statistics and confidence intervals, and performing hypothesis tests for statistical inference. It does this using a combination of functions that are built with the emphasis on clear expressive code and using correct statistical grammar that explains the way the values are calculated and the tests are evaluated in statistical inference.

With this package as the inspiration, `pyfer` will have four main functions (`specify`,`generate`,`calculate`,`get_ci`) for the first iteration. These functions will, given a data frame and the specified response variable; calculate summary statistics and confidence intervals for the response variable. Further details follow in the description of the functions below.

### Where does `pyfer` fit into the Python ecosystem?

Currently, there isn't a package in Python's ecosystem that does a great job at replicating the `infer` package's functionality, easy-of-use, and use of expressive statistical grammar. Pyfer fills that gap and provides the basic tools to perform statistical inference in Python.

## Installing `pyfer`

To install using pip, on your command line type:

`pip install git+https://github.com/UBC-MDS/pyfer.git`

## Functions & Usage

**specify(data, response, explanatory)**  


    Choose specific columns to feed the subsequent pipeline.

    Parameters:
    ---------------
    data: pd.DataFrame
    response: string
        One column of the dataframe to be the response variable.
    explanatory: string or list of strings
        Columns to be the explanatory variables

    Returns:
    ---------------
    pd.DataFrame:
        Dataframe containing one column for response variable and zero or more columns for the explanatory variables. The first column is always the response.


**generate(data, n_samples, type="boostrap")**  


    Generate bootstrap resamples and permutations

    Parameters:
    ---------------
    data: pd.DataFrame
        A Dataframe containing a response column (the first one) and zero or more explanatory columns. Usually the output of a specify function.
    n_samples: integer
        Number of resamples.
    type: string
        "Bootstrap" (default), or "Permutation".

    Returns:
    ---------------
    pd.DataFrame:
        Dataframe containing all resamples stacked vertically. Will keep all columns from the input data and an additional sample_id column to identify individual resamples.


**calculate(data, stat="mean")**  


    Calculate a summarizing statistic for each bootstrap sample.

    Parameters:
    ---------------
    data: pd.DataFrame
        A Dataframe generated from `generate` function with columns: response, sample_id and zero or more explanatory variables.
    columns: string or list of strings
        Column(s) that will be subsetted from the dataframe and summarized by 'stat'.
    stat: string
        "mean" (default) or "median"(leave for further exploration)

    Returns:
    ---------------
    pd.DataFrame:
        Summarized data. Each row contains the summary statistic for a given resample.


**get_ci(data, level=0.95, point_estimate=None)**  


    Return the bootstrap confidence interval for a point estimate.

    Parameters:
    ---------------
    data: pd.DataFrame
        A Dataframe containing summarizing statistics from multiple resamples. Typically it's the output of a `calculate` function.
    level: float
        Significance level of the confidence interval. Example: 0.05 (default) represents the 95% confidence interval.
	point_estimate: float
		A float representing the value of the point estimate that is input by the user. Note: not implemented as of writing.


    Returns:
    ---------------
    pd.DataFrame
        Dataframe containing 1 row and columns for Statistic (Point Estimate), Significance Level, Lower Bound and Upper Bound.


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
