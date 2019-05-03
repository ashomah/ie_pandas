from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_mixed_in_np_rowindex_both_index_axis():
    obj = np.array([30, 53.0, "31", True, 32])
    df = DataFrame(
        obj, rowindex=["AGE"], colindex=["A", "B", "C", "D", "E"], axis=1
    )

    expected_output = ["AGE"]

    actual_output = df.rowindex

    assert actual_output == expected_output
