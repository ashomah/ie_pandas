from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_int_in_dict_of_np_colindex_row_index():
    obj = {"age": np.array([30, 53, 31, 47, 32]), "albums": np.array([4, 10, 2, 5, 4])}
    df = DataFrame(obj, rowindex=["A", "B", "C", "D", "E"])

    expected_output = ["age", "albums"]

    actual_output = df.colindex

    assert actual_output == expected_output
