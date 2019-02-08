import pandas as pd

def generate(data, n_samples, type="boostrap"):
    '''
    Generate bootstrap resamples and permutations

    Parameters:
    data (pd.DataFrame): a Dataframe generated from a specify function.
    n_samples (int): Number of resamples.
    type (str): "Bootstrap" (default), or "Permutation".

    Returns:
    (pd.DataFrame): Dataframe containing columns for response, sample_id and, if specified, explanatory variables.
    '''
    return pd.DataFrame()
