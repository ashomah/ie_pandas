from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_int_in_np_repr_both_index():
    obj = np.array([30, 53, 31, 47, 32])
    df = DataFrame(obj, colindex=["AGE"], rowindex=["A", "B", "C", "D", "E"])

    expected_output = (
        "   AGE"
        + "\n"
        + "A   30"
        + "\n"
        + "B   53"
        + "\n"
        + "C   31"
        + "\n"
        + "D   47"
        + "\n"
        + "E   32"
    )

    actual_output = repr(df)

    assert actual_output == expected_output
