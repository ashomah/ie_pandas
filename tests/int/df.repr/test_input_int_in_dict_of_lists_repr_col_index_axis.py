from ie_pandas import DataFrame
import pytest


def test_input_int_in_dict_of_lists_repr_col_index_axis():
    obj = {"age": [30, 53, 31, 47, 32], "albums": [4, 10, 2, 5, 4]}
    df = DataFrame(obj, colindex=["V", "W", "X", "Y", "Z"], axis=1)

    expected_output = (
        "         V   W   X   Y   Z"
        + "\n"
        + "age     30  53  31  47  32"
        + "\n"
        + "albums   4  10   2   5   4"
    )

    actual_output = repr(df)

    assert actual_output == expected_output
