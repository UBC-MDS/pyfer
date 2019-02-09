import pytest
import pandas as pd
from functions import generate

def test_shape_output():
  '''
  Test number of rows and columns in the output match
  '''
  # import pdb
  # pdb.set_trace()
  df_input = pd.DataFrame(columns=["Response"], data=[1,2,3])
  df_output = generate(data=df_input, n_samples=3)

  assert df_output.shape == (9,1)

def test_empty_dataframe():
  '''
  Test function response with an emtpy dataframe
  '''
  pass

def test_zero_n_samples():
  '''
  Test function response with when n_samples = 0
  '''
  pass

def test_samples_exist():
  '''
  Test whether all bootstrap values exist in the original sample.
  '''
  pass

def test_overflow():
  '''
  Test function behavior when number of samples is too high.
  '''
  pass
