import pytest
import pandas as pd
from .functions import specify




def test_output_shape():
    '''
    Test that the output dataframe is of correct shape
    (response columns plus explanatory variables)
    '''
    df_input = pd.DataFrame(columns=["response", "unused_col",
                                     "explan1", "explan2", "unused_col2"],
                            data=[[1,2,3,4,5],
                                  [2,3,4,5,6],
                                  [3,4,5,6,7]])
    df_output = specify(data=df_input,
                        response="response",
                        explanatory=["explan1", "explan2"])

    assert df_output.shape == (len(df_input),)

def test_expected_output():
    '''
    Test that the resulting dataframe is returning the expected column(s)
    '''
    df_input = pd.DataFrame(columns=["response", "unused_col"],
                            data=[[1,2],[2,3],[3,4]])
    df_output = specify(data=df_input, response="response")

    assert df_output.columns == "response"

def test_wrong_response_col():
    '''
    Test that function raises error if provided response column is not
    in dataframe
    '''
    df_input = pd.DataFrame(columns=["response", "unused_col"],
                            data=[[1,2],[2,3],[3,4]])
    with pytest.raises(Exception):
        df_output = specify(data=df_input, response="asdfasdf")
