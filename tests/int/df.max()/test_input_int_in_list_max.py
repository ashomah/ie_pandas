from ie_pandas import DataFrame
import pytest


def test_input_int_in_list_max():
    obj = [30, 53, 31, 47, 32]
    df = DataFrame(obj, colindex=["AGE"], rowindex=["A", "B", "C", "D", "E"])

    expected_output = [53]

    actual_output = df.max()

    assert actual_output == expected_output
