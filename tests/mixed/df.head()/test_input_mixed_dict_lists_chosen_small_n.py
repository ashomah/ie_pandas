from ie_pandas import DataFrame
import pytest


def test_input_mixed_in_dict_of_lists_head():
    obj = {
        "age": [30.1, 53.1, 31.1, 47.1, 32.1],
        "albums": [4, 10, 2, 5, 4],
        "C": ["a", "b", "c", "d", "e"],
        "D": [True, False, True, True, False],
    }

    df = DataFrame(obj)

    actual_output = repr(df.head(2))

    expected_output = (
        "    AGE  ALBUMS  C      D"
        + "\n"
        + "A  30.1       4  a   True"
        + "\n"
        + "B  53.1      10  b  False"
    )

    assert actual_output == expected_output

