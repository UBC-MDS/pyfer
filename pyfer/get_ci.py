import pandas as pd
import numpy as np

def get_ci(data, interval=range(0,100)):
    '''
    Return the bootstrap confidence interval for a point estimate.

    Parameters:
    data (pd.DataFrame): a Dataframe generated from a specify function.
    interval (float): 95 (default), or any float between 0 and 100

    Returns:
    (pd.DataFrame): Dataframe containing 1 row and columns for Statistic (Point Estimate), Lower Bound, Upper Bound
    '''
    return pd.DataFrame()
