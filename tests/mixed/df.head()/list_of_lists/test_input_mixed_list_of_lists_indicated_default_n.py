from ie_pandas import DataFrame
import pytest


def test_input_mixed_in_list_of_lists_head():
    obj = [
        [30.1, 53.1, 31.1, 47.1, 32.1],
        [4, 10, 2, 5, 4],
        ["a", "b", "c", "d", "e"],
        [True, False, True, True, False],
    ]
    df = DataFrame(obj)

    expected_output = (
        "      0   1  2      3"
        + "\n"
        + "0  30.1   4  a   True"
        + "\n"
        + "1  53.1  10  b  False"
        + "\n"
        + "2  31.1   2  c   True"
        + "\n"
        + "3  47.1   5  d   True"
        + "\n"
        + "4  32.1   4  e  False"
    )

    actual_output = repr(df.head(5))

    assert actual_output == expected_output

