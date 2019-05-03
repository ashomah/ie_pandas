from ie_pandas import DataFrame
import pytest


def test_input_int_in_dict_of_lists_colindex_both_index_axis():
    obj = [[30, 53, 31, 47, 32], [4, 10, 2, 5, 4]]
    df = DataFrame(
        obj,
        rowindex=["AGE", "ALBUMS"],
        colindex=["A", "B", "C", "D", "E"],
        axis=1,
    )

    expected_output = ["A", "B", "C", "D", "E"]

    actual_output = df.colindex

    assert actual_output == expected_output
