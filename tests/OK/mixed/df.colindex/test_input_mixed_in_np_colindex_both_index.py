from ie_pandas import DataFrame
import pytest
import numpy as np

def test_input_mixed_in_np_colindex_both_index():
    obj = np.array([30, 53.0, '31', True, 32])
    df = DataFrame(obj, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    expected_output = ['AGE']

    actual_output = df.colindex

    assert actual_output == expected_output