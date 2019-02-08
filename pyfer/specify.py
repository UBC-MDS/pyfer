import pandas as pd

def specify(data, response="str"):
    '''
    Choose specific columns to feed the subsequent pipeline

    Parameters:
    data (pd.DataFrame): a Dataframe contains severval columns.
    response（str）： One column of the dataframe to be the response variable.

    Returns:
    (pd.DataFrame): Dataframe containing 1 column for response variable
    '''
    return pd.DataFrame()
