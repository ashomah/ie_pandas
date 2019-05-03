from ie_pandas import DataFrame
import pytest


def test_input_mixed_in_list_of_lists_df_no_index():
    obj = [
        [30.1, 53.1, 31.1, 47.1, 32.1],
        [4, 10, 2, 5, 4],
        ["a", "b", "c", "d", "e"],
        [True, False, True, True, False],
    ]
    df = DataFrame(obj)

    expected_output = {
        "0": [30.1, 53.1, 31.1, 47.1, 32.1],
        "1": [4, 10, 2, 5, 4],
        "2": ["a", "b", "c", "d", "e"],
        "3": [True, False, True, True, False],
    }

    actual_output = df.df

    assert actual_output == expected_output
