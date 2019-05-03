from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_mixed_in_np_repr_row_index():
    obj = np.array([30, 53.0, "31", True, 32])
    df = DataFrame(obj, rowindex=["A", "B", "C", "D", "E"])

    expected_output = (
        "      0"
        + "\n"
        + "A    30"
        + "\n"
        + "B  53.0"
        + "\n"
        + "C    31"
        + "\n"
        + "D  True"
        + "\n"
        + "E    32"
    )

    actual_output = repr(df)

    assert actual_output == expected_output
