from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_int_in_np_mean():
    obj = np.array([30, 53, 31, 47, 32])
    df = DataFrame(obj, colindex=["AGE"], rowindex=["A", "B", "C", "D", "E"])

    expected_output = [38.6]

    actual_output = df.mean()

    assert actual_output == expected_output
