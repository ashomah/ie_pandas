from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_int_in_np_colindex_row_index():
    obj = np.array([30, 53, 31, 47, 32])
    df = DataFrame(obj, rowindex=["A", "B", "C", "D", "E"])

    expected_output = ["0"]

    actual_output = df.colindex

    assert actual_output == expected_output
