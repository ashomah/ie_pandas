from ie_pandas import DataFrame
import pytest


def test_input_int_in_dict_of_lists_rowindex_both_index_axis():
    obj = {"age": [30, 53, 31, 47, 32], "albums": [4, 10, 2, 5, 4]}
    df = DataFrame(
        obj,
        rowindex=["AGE", "ALBUMS"],
        colindex=["A", "B", "C", "D", "E"],
        axis=1,
    )

    expected_output = ["AGE", "ALBUMS"]

    actual_output = df.rowindex

    assert actual_output == expected_output
