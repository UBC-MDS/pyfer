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
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input should be a Pandas DataFrame")
    if not isinstance(response, str):
        raise TypeError("Response should be of type str")

    columns = [response]

    if explanatory:
        columns.extend(explanatory)
        
    df_output = data[columns]

    return df_output

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

def get_ci(data, level=0.95, point_estimate=None):
    '''
    Return the bootstrap confidence interval for a point estimate.

    Parameters:
    ---------------
    data: pd.DataFrame
        A Dataframe containing summarizing statistics from multiple resamples. Typically it's the output of a `calculate` function. Should have a column called 'stat'.
    level: float
        Numerical value representing the confidence interval. Example: 0.95 (default) represents the 95% confidence interval.

    Returns:
    ---------------
    pd.DataFrame
        Dataframe containing 1 row and columns for Statistic (Point Estimate), significance level, Lower Bound and Upper Bound.
    '''
        
    #Checking if input is dataframe
    if not isinstance(data,pd.DataFrame):
        raise TypeError("Input should be a Pandas dataframe")
    
    #Checking if level is float/int
    if not isinstance(level,float):
        if not (level == 0 or level == 1):
            raise TypeError("Level should be of type: float or 0,1")
    
    #Checking if level is within range
    if (level < 0 or level > 1):
        raise ValueError("Level should be a value between 0 and 1")
    
    quant_arr = np.array([(1-level)/2,level+((1-level)/2)])
    
    # Make sure 'stat' is in calculate function
    X_n = data['stat'].quantile(quant_arr)
    
    X_t = pd.DataFrame(X_n)
    X_t = X_t.transpose()
    X_t['Point Estimate'] = data['stat'].mean() #Ask about this
    X_i = X_t.set_index([pd.Index([level])])
    X_i.index.name = "Confidence Level"
    #X_i.rename(columns = {X_i.columns[0]:round(X_i.columns[0],3),X_i.columns[1]:round(X_i.columns[1],3)},inplace=True)
    X_i.rename(columns = {X_i.columns[0]:"Lower Bound",X_i.columns[1]:"Upper Bound"},inplace=True)
    
    return X_i
