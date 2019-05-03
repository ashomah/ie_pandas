from ie_pandas import DataFrame
import pytest
import numpy as np

def test_input_int_in_np_colindex_col_index():
    obj = np.array([30, 53, 31, 47, 32])
    df = DataFrame(obj, colindex = ['AGE'])

    expected_output =  ['AGE']

    actual_output = df.colindex

    assert actual_output == expected_output