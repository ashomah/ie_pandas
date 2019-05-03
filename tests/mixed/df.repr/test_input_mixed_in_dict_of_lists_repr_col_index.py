from ie_pandas import DataFrame
import pytest


def test_input_mixed_in_dict_of_lists_repr_col_index():
    obj = {
        "age": [30.1, 53.1, 31.1, 47.1, 32.1],
        "albums": [4, 10, 2, 5, 4],
        "C": ["a", "b", "c", "d", "e"],
        "D": [True, False, True, True, False],
    }
    df = DataFrame(obj, colindex=["AGE", "ALBUMS", "C", "D"])

    expected_output = (
        "    AGE  ALBUMS  C      D"
        + "\n"
        + "0  30.1       4  a   True"
        + "\n"
        + "1  53.1      10  b  False"
        + "\n"
        + "2  31.1       2  c   True"
        + "\n"
        + "3  47.1       5  d   True"
        + "\n"
        + "4  32.1       4  e  False"
    )

    actual_output = repr(df)

    assert actual_output == expected_output
