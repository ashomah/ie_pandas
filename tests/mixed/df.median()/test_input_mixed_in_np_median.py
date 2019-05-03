from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_mixed_in_np_median_odd():
    obj = np.array([30, 53.0, "31", True, 32, 100])
    df = DataFrame(
        obj, colindex=["AGE"], rowindex=["A", "B", "C", "D", "E", "F"]
    )

    expected_output = []

    actual_output = df.median()

    assert actual_output == expected_output


def test_input_mixed_in_np_median_even():
    obj = np.array([30, 53.0, "31", True, 32])
    df = DataFrame(obj, colindex=["AGE"], rowindex=["A", "B", "C", "D", "E"])

    expected_output = []

    actual_output = df.median()

    assert actual_output == expected_output
