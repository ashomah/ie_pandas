from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_mixed_in_np_repr_col_index():
    obj = np.array([30, 53.0, "31", True, 32])
    df = DataFrame(obj, colindex=["AGE"])

    expected_output = (
        "    AGE"
        + "\n"
        + "0    30"
        + "\n"
        + "1  53.0"
        + "\n"
        + "2    31"
        + "\n"
        + "3  True"
        + "\n"
        + "4    32"
    )

    actual_output = repr(df)

    assert actual_output == expected_output
