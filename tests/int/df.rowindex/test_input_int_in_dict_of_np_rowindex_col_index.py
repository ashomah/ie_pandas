from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_int_in_dict_of_np_rowindex_col_index():
    obj = {
        "age": np.array([30, 53, 31, 47, 32]),
        "albums": np.array([4, 10, 2, 5, 4]),
    }
    df = DataFrame(obj, colindex=["AGE", "ALBUMS"])

    expected_output = ["0", "1", "2", "3", "4"]

    actual_output = df.rowindex

    assert actual_output == expected_output
