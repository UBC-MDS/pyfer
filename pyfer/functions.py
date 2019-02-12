import pandas as pd
import numpy as np

def specify(data, response, explanatory=None):
    '''
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
    '''
    output = data[response]
    return pd.DataFrame(output)

def generate(data, n_samples, type="boostrap"):
    '''
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
    '''
    return

def calculate(data, stat="mean"):
    '''
    Calculate a summarizing statistic for each bootstrap sample.

    Parameters:
    ---------------
    data: pd.DataFrame
        A Dataframe generated from `generate` function with columns: response, sample_id and zero or more explanatory variables.
    stat: string
        "mean" (default) or "median".

    Returns:
    ---------------
    pd.DataFrame:
        Summarized data. Each row contains the summary statistic for a given resample.
    '''
    return

def get_ci(data, alpha=0.05, point_estimate=None):
    '''
    Return the bootstrap confidence interval for a point estimate.

    Parameters:
    ---------------
    data: pd.DataFrame
        A Dataframe containing summarizing statistics from multiple resamples. Typically it's the output of a `calculate` function.
    interval: float
        Significance level of the confidence interval. Example: 0.05 (default) represents the 95% confidence interval.

    Returns:
    ---------------
    pd.DataFrame
        Dataframe containing 1 row and columns for Statistic (Point Estimate), significance level, Lower Bound and Upper Bound.
    '''
    return
