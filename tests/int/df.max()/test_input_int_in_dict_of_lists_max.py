from ie_pandas import DataFrame
import pytest


def test_input_int_in_dict_of_lists_max():
    obj = {"age": [30, 53, 31, 47, 32], "albums": [4, 10, 2, 5, 4]}
    df = DataFrame(obj, colindex=["AGE", "ALBUMS"], rowindex=["A", "B", "C", "D", "E"])

    expected_output = [53, 10]

    actual_output = df.max()

    assert actual_output == expected_output
