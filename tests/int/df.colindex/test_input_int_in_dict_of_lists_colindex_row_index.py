from ie_pandas import DataFrame
import pytest


def test_input_int_in_dict_of_lists_colindex_row_index():
    obj = {"age": [30, 53, 31, 47, 32], "albums": [4, 10, 2, 5, 4]}
    df = DataFrame(obj, rowindex=["A", "B", "C", "D", "E"])

    expected_output = ["age", "albums"]

    actual_output = df.colindex

    assert actual_output == expected_output
