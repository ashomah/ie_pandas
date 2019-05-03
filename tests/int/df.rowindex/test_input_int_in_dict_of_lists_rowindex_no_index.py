from ie_pandas import DataFrame
import pytest


def test_input_int_in_dict_of_lists_rowindex_no_index():
    obj = {"age": [30, 53, 31, 47, 32], "albums": [4, 10, 2, 5, 4]}
    df = DataFrame(obj)

    expected_output = ["0", "1", "2", "3", "4"]

    actual_output = df.rowindex

    assert actual_output == expected_output
