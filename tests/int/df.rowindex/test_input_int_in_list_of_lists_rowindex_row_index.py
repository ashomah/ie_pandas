from ie_pandas import DataFrame
import pytest


def test_input_int_in_list_of_lists_rowindex_row_index():
    obj = [[30, 53, 31, 47, 32], [4, 10, 2, 5, 4]]
    df = DataFrame(obj, rowindex=["A", "B", "C", "D", "E"])

    expected_output = ["A", "B", "C", "D", "E"]

    actual_output = df.rowindex

    assert actual_output == expected_output
