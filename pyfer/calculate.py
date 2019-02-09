import pandas as pd
import numpy as np

def calculate(data, stat=("mean"):
    '''
    Calculate a summarizing statistic for each bootstrap sample.

    Parameters:
    data (pd.DataFrame): a Dataframe generated from `generate` function which has 2 columns: response, sample_id
    stat (str): "mean" (default), or "median".

    Returns:
    (pd.DataFrame): Dataframe containing number of sample_id rows and 2 columns: stat(mean or median), sample_id
    '''
    return pd.DataFrame()
