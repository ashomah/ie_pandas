from ie_pandas import DataFrame
import pytest


def test_input_mixed_in_list_of_lists_sum():
    obj = [
        [30.1, 53.1, 31.1, 47.1, 32.1],
        [4, 10, 2, 5, 4],
        ["a", "b", "c", "d", "e"],
        [True, False, True, True, False],
    ]
    df = DataFrame(
        obj,
        colindex=["AGE", "ALBUMS", "C", "D"],
        rowindex=["A", "B", "C", "D", "E"],
    )

    expected_output = [193.5, 25, 3]

    actual_output = df.sum()

    assert actual_output == expected_output
