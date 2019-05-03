from ie_pandas import DataFrame
import pytest


def test_bool_input_in_list_of_lists():
    artists_list_of_lists = [[True, False, True], [False, True, False]]
    list_of_lists_df = DataFrame(artists_list_of_lists, colindex=["age", "albums"])

    expected_output = (
        "     age  albums"
        + "\n"
        + "0   True   False"
        + "\n"
        + "1  False    True"
        + "\n"
        + "2   True   False"
    )

    actual_output = repr(list_of_lists_df)

    assert actual_output == expected_output
