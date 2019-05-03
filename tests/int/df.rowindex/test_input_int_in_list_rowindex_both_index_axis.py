from ie_pandas import DataFrame
import pytest


def test_input_int_in_list_rowindex_both_index_axis():
    obj = [30, 53, 31, 47, 32]
    df = DataFrame(obj, rowindex=["AGE"], colindex=["A", "B", "C", "D", "E"], axis=1)

    expected_output = ["AGE"]

    actual_output = df.rowindex

    assert actual_output == expected_output
