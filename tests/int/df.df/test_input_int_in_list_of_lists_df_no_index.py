from ie_pandas import DataFrame
import pytest


def test_input_int_in_list_of_lists_df_no_index():
    obj = [[30, 53, 31, 47, 32], [4, 10, 2, 5, 4]]
    df = DataFrame(obj)

    expected_output = {"0": [30, 53, 31, 47, 32], "1": [4, 10, 2, 5, 4]}

    actual_output = df.df

    assert actual_output == expected_output
