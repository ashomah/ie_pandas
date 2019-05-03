from ie_pandas import DataFrame
import pytest
import numpy as np

def test_input_int_in_np_df_col_index():
    obj = np.array([30, 53, 31, 47, 32])
    df = DataFrame(obj, colindex = ['AGE'])

    expected_output =  {'AGE': [30, 53, 31, 47, 32]}

    actual_output = df.df

    assert actual_output == expected_output