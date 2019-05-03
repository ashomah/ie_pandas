from ie_pandas import DataFrame
import pytest
import numpy as np

def test_input_int_in_np_repr_both_index_axis():
    obj = np.array([30, 53, 31, 47, 32])
    df = DataFrame(obj, rowindex = ['AGE'], colindex = ['A', 'B', 'C', 'D', 'E'], axis=1)

    expected_output = "      A   B   C   D   E" + "\n" + \
                      "AGE  30  53  31  47  32"

    actual_output = repr(df)

    assert actual_output == expected_output