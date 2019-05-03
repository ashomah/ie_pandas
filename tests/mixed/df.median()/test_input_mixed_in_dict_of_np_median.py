from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_mixed_in_dict_of_np_median_odd():
    obj = {
        "age": np.array([30.1, 53.1, 31.1, 47.1, 32.1]),
        "albums": np.array([4, 10, 2, 5, 4]),
        "C": np.array(["a", "b", "c", "d", "e"]),
        "D": np.array([True, False, True, True, False]),
    }
    df = DataFrame(
        obj,
        colindex=["AGE", "ALBUMS", "C", "D"],
        rowindex=["A", "B", "C", "D", "E"],
    )

    expected_output = [32.1, 4.0, 1.0]

    actual_output = df.median()

    assert actual_output == expected_output


def test_input_mixed_in_dict_of_np_median_even():
    obj = {
        "age": np.array([30.1, 53.1, 31.1, 47.1, 32.1, 100.0]),
        "albums": np.array([4, 10, 2, 5, 4, 100]),
        "C": np.array(["a", "b", "c", "d", "e", "f"]),
        "D": np.array([True, False, True, True, False, True]),
    }
    df = DataFrame(
        obj,
        colindex=["AGE", "ALBUMS", "C", "D"],
        rowindex=["A", "B", "C", "D", "E", "F"],
    )

    expected_output = [39.6, 4.5, 1.0]

    actual_output = df.median()

    assert actual_output == expected_output
