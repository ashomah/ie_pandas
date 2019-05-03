from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_mixed_in_dict_of_np_repr_col_index():
    obj = {
        "age": np.array([30.1, 53.1, 31.1, 47.1, 32.1]),
        "albums": np.array([4, 10, 2, 5, 4]),
        "C": np.array(["a", "b", "c", "d", "e"]),
        "D": np.array([True, False, True, True, False]),
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
