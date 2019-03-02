import pytest
import pandas as pd
from pyfer.functions import specify, generate, calculate, get_ci

class TestSpecify():

    def test_output_shape(self):
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

        assert df_output.shape == (len(df_input), 3)

    def test_expected_output(self):
        '''
        Test that the resulting dataframe is returning the expected column(s)
        '''
        df_input = pd.DataFrame(columns=["response", "unused_col"],
                                data=[[1,2],[2,3],[3,4]])
        df_output = specify(data=df_input, response="response")

        assert df_output.columns.tolist() == ["response"]

    def test_wrong_response_col(self):
        '''
        Test that function raises error if provided response column is not
        in dataframe
        '''
        df_input = pd.DataFrame(columns=["response", "unused_col"],
                                data=[[1,2],[2,3],[3,4]])
        with pytest.raises(Exception):
            df_output = specify(data=df_input, response="asdfasdf")


class TestGenerate():
    def test_shape_output(self):
        '''
        Test number of rows and columns in the output match
        '''
        df_input = pd.DataFrame(columns=["response"], data=[1,2,3])
        df_output = generate(data=df_input, n_samples=3)

        assert df_output.shape == (9,2)

    def test_empty_dataframe(self):
        '''
        Test function response with an emtpy dataframe, expect error.
        '''
        df_input = pd.DataFrame()
        with pytest.raises(Exception):
            df_output = generate(data=df_input, n_samples=3)

    def test_non_positive_n_samples(self):
        '''
        Test function response with when n_samples = 0, expect empty DataFrame
        '''
        df_input = pd.DataFrame(columns=["response"], data=[1,2,3])
        with pytest.raises(Exception):
            df_output = generate(data=df_input, n_samples=0)

    def test_samples_exist(self):
        '''
        Test whether all bootstrap values exist in the original sample.
        '''
        df_input = pd.DataFrame(columns=["response"], data=[1,2,3])
        df_output = generate(data=df_input, n_samples=3)

        assert df_output.response.isin(df_input.response).all()

    def test_overflow(self):
        '''
        Test function behavior when number of samples is too high.
        '''
        df_input = pd.DataFrame(columns=["response"], data=[1])
        with pytest.raises(Exception):
          df_output = generate(data=df_input, n_samples=1e10000000)

class TestCalculate:
    def test_shape_output(self):
        '''
        Test that the output's shape is coming out as expected.
        '''
        df_input = pd.DataFrame(columns=["response", "sample_id"],
                              data=[[1,1],[2,1],[2,2],[3,2],[3,3],[4,3]])
        df_output = calculate(df_input)
        # Since the calculate is taking the output of generate as input,
        # the shape of the input should be (n,2), and the test data shape is (6,2)
        # Hence, the output shape should be (# of sample_id, 2)

        assert df_output.shape == (3,2)

    def test_output_statistic(self):
        '''
        Test that the output's statistic is coming out as expected.
        '''
        df_input = pd.DataFrame(columns=["response", "sample_id"],
                              data=[[1,1],[2,1],[2,2],[3,2],[3,3],[4,3]])
        df_output = calculate(df_input)
        assert df_output['stat'].dtype == "float64"
        assert df_output.loc[df_output['sample_id']==3]['stat'][2] == 3.5

    def test_empty_dataframe(self):
        '''
        Test function response with an emtpy dataframe, expect error.
        '''
        df_input = pd.DataFrame()
        with pytest.raises(Exception):
            df_output = calculate(data=df_input)

    def test_statistic_not_implemented(self):
        '''
        Test function response with a statistic that has not been implemented
        '''
        df_input = pd.DataFrame()
        with pytest.raises(Exception):
            df_output = calculate(data=df_input, stat="asdfasdf")

class TestGet_ci():

    def test_output_is_dataframe(self):
        '''
        Test that output is a pd.DataFrame, not pd.Series
        '''
        df_input = pd.DataFrame(columns=["stat", "sample_id"],
                          data=[
                          [1,1],[2,2],[3,3],[4,4],[5,5],
                          ])
        df_output = get_ci(df_input, level=0.8)

        assert isinstance(df_output, pd.DataFrame)

    def test_output_shape(self):
        '''
        Test that output shape comes out as expected
        '''
        df_input = pd.DataFrame(columns=["stat", "sample_id"],
                          data=[
                          [1,1],[2,2],[3,3],[4,4],[5,5],
                          [6,6],[7,7],[8,8],[9,9],[10,10],
                          ])
        df_output = get_ci(df_input, level=0.8)

        assert df_output.shape == (1,4)

    def test_correct_bounds(self):
        '''
        Test that bounds are coming out as expected
        '''
        df_input = pd.DataFrame(columns=["stat", "sample_id"],
                          data=[[0,0],
                          [1,1],[2,2],[3,3],[4,4],[5,5],
                          [6,6],[7,7],[8,8],[9,9],[10,10]
                          ])
        df_output = get_ci(df_input, level=0.8)

        assert df_output['lower_bound'].iloc[0] == pytest.approx(1.0)
        assert df_output['upper_bound'].iloc[0] == pytest.approx(9.0)

    def test_wrong_signif_level(self):
        '''
        Test that error is thrown when significance levels are implausible
        '''
        df_input = pd.DataFrame(columns=["stat", "sample_id"],
                          data=[
                          [1,1],[2,2],[3,3],[4,4],[5,5],
                          [6,6],[7,7],[8,8],[9,9],[10,10],
                          ])
        with pytest.raises(Exception):
            df_output = get_ci(df_input, alpha=1.3)

    #def test_point_estimate(self):
    #    '''
    #    Test that the point estimate is being reported correctly.
    #    '''
    #    df_input = pd.DataFrame(columns=["mean", "sample_id"],
    #                      data=[
    #                      [1,1],[2,2],[3,3],[4,4],[5,5],
    #                      [6,6],[7,7],[8,8],[9,9],[10,10],
    #                      ])
    #    df_output = get_ci(df_input, point_estimate=3.5)

    #    assert df_output.point_estimate.iloc[0] == pytest.approx(3.5)
