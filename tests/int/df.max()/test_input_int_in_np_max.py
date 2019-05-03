from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_int_in_np_max():
    obj = np.array([30, 53, 31, 47, 32])
    df = DataFrame(obj, colindex=["AGE"], rowindex=["A", "B", "C", "D", "E"])

    expected_output = [53]

    actual_output = df.max()

    assert actual_output == expected_output
