from ie_pandas import DataFrame
import pytest


def test_input_mixed_in_dict_of_lists_colindex_no_index():
    obj = {
        "age": [30.1, 53.1, 31.1, 47.1, 32.1],
        "albums": [4, 10, 2, 5, 4],
        "C": ["a", "b", "c", "d", "e"],
        "D": [True, False, True, True, False],
    }
    df = DataFrame(obj)

    expected_output = ["age", "albums", "C", "D"]

    actual_output = df.colindex

    assert actual_output == expected_output
