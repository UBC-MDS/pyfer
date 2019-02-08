# Since the calculate is taking the output of generate as input,
# the shape of the input should be (n,2), and the test data shape is (200,2)
# Hence, the output shape should be (# of sample_id, 2)

import pytest
import pandas as pd
from calculate import calculate



def test_calculate(calculate,df):
  df = pd.read_csv("test_data_calculate.csv") 
  df_output = calculate(df)

  '''
  Test if the `calculate` function is working properly
    
  Parameters:
  `calculate`: 
      The function being test
  df: dataFrame
      A Data frame using for test, which only contains 2 columns: sample_id, reponse
        
  Returns:
  string:  
    "All tests pass. Success!" if all test are passed
    Raising error if some test is not passed.
    '''
    assert type(df_output) == "pandas.core.frame.DataFrame", "The type of the output is wrong"
    assert df_output.shape == (10,2), "The shape of the output is wrong" 
    assert type(df_output['mean'][0])== "numpy.int64", "The type of the output value is wrong"
    assert df_output['mean'][3] == 38.85, "The calculate mean is wrong"
    print("All test passed") 



