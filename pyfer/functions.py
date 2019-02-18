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

def generate(data, n_samples, type="bootstrap"):
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
    if type not in ("bootstrap"):
        raise ValueError("The only choice for argument 'type' is 'bootstrap', for now")

    df_output = pd.DataFrame()

    if type == "bootstrap":
        for i in range(n_samples):
            bootstrap_sample = data.sample(n=len(data), replace=True)
            bootstrap_sample["sample_id"] = i
            df_output = pd.concat([df_output, bootstrap_sample])
            df_output.reset_index(inplace=True, drop=True)

    return df_output

def calculate(data, stat="mean"):
    '''
    Calculate a summarizing statistic for each bootstrap sample.

    Parameters:
    ---------------
    data: pd.DataFrame
        A Dataframe generated from `generate` function with columns: response, sample_id and zero or more explanatory variables.
    stat: string
        "mean" (default) or "median"(leave for further exploration)

    Returns:
    ---------------
    pd.DataFrame:
        Summarized data. Each row contains the summary statistic for a given resample.
    '''
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input should be a Pandas DataFrame")
    if stat=="Mean":
        raise TypeError("Input is incorrect. Did you mean 'mean'?")
    if stat=="Median":
        raise TypeError("Input is incorrect. Did you mean 'median'?")
    if stat != "mean": raise Exception
    data=data.groupby(['sample_id'], as_index=False).mean()
    data.columns=['sample_id','stat']
    # if stat=="mean":
    #    data['stat']=""
    #    for i in range(1, data['sample_id'].max()+1):
    #        stat_per_sample=data['response'][data['sample_id']==i].mean()
    #        data.loc[data['sample_id']==i,'stat'] = stat_per_sample

    return data

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
    X_t['point_estimate'] = point_estimate
    X_t['significance_level'] = level
    X_t.reset_index(inplace=True, drop=True)
    X_t.rename(columns = {X_t.columns[0]:"lower_bound",X_t.columns[1]:"upper_bound"},inplace=True)

    return X_t
