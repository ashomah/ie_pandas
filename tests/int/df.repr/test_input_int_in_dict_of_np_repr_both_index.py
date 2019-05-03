from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_int_in_dict_of_np_repr_both_index():
    obj = {
        "age": np.array([30, 53, 31, 47, 32]),
        "albums": np.array([4, 10, 2, 5, 4]),
    }
    df = DataFrame(
        obj, colindex=["AGE", "ALBUMS"], rowindex=["A", "B", "C", "D", "E"]
    )

    expected_output = (
        "   AGE  ALBUMS"
        + "\n"
        + "A   30       4"
        + "\n"
        + "B   53      10"
        + "\n"
        + "C   31       2"
        + "\n"
        + "D   47       5"
        + "\n"
        + "E   32       4"
    )

    actual_output = repr(df)

    assert actual_output == expected_output
