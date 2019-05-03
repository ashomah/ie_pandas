from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_int_in_dict_of_np_min():
    obj = {
        "age": np.array([30, 53, 31, 47, 32]),
        "albums": np.array([4, 10, 2, 5, 4]),
    }
    df = DataFrame(
        obj, colindex=["AGE", "ALBUMS"], rowindex=["A", "B", "C", "D", "E"]
    )

    expected_output = [30, 2]

    actual_output = df.min()

    assert actual_output == expected_output
