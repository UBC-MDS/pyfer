# Since the get_ci is taking the output of calculate as input,
# the shape of the input should be (n,2), and the test data shape is (1000,2)
# Hence, the output shape should be (3, 1)



import pytest
import pandas as pd
from get_ci import get_ci

def test_get_ci(get_ci,df,n):
  df = pd.read_csv("test_data_get_ci.csv") 
  df_output = get_ci(df, n)
  '''
  Test if the `get_ci` function is working properly
    
  Parameters:
  `test_get_ci`: 
      The function being test
  df: dataFrame
      A Data frame using for test, which only contains 2 columns: sample_id, reponse
        
  Returns:
  string:  
      "All tests pass. Success!" if all test are passed
      Raising error if some test is not passed.
  '''
  assert type(n)== "numpy.int64" or type(n)== "float", "The type of interval is wrong"
  assert n <= 100 or n>=0, "The value of interval should be in (0,100)"
  assert type(df_output) == "pandas.core.frame.DataFrame", "The type of the output is wrong"
  assert df_output.shape == (3,1), "The shape of the output is wrong" 
  assert type(df_output['mean'][0])== "numpy.int64", "The type of the output value is wrong"
  assert df_output['mean']== 38.559, "The value of point estimate is wrong"
  assert get_ci(df, 95)['lower_bound] == 30, "The value of lower bound is wrong"
  assert get_ci(df, 95)['upper_bound] == 42, "The value of upper bound is wrong"
  print("All test passed") 


