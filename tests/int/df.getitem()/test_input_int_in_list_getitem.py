from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_int_in_list_getitem_by_index():
    obj = [30, 53, 31, 47, 32]
    df = DataFrame(obj, colindex=["AGE"], rowindex=["A", "B", "C", "D", "E"])

    expected_output = np.array([30, 53, 31, 47, 32])

    actual_output = df[0]

    assert np.all(actual_output == expected_output)


def test_input_int_in_list_getitem_by_rowindex():
    obj = [30, 53, 31, 47, 32]
    df = DataFrame(obj, colindex=["AGE"], rowindex=["A", "B", "C", "D", "E"])

    expected_output = np.array([30, 53, 31, 47, 32])

    actual_output = df["AGE"]

    assert np.all(actual_output == expected_output)


def test_input_int_in_list_getitem_wrong():
    obj = [30, 53, 31, 47, 32]
    df = DataFrame(obj, colindex=["AGE"], rowindex=["A", "B", "C", "D", "E"])

    with pytest.raises(Exception) as exc_info:
        df[100]

    exception_raised = exc_info.value

    assert exception_raised


def test_input_int_in_list_getitem_empty():
    obj = [30, 53, 31, 47, 32]
    df = DataFrame(obj, colindex=["AGE"], rowindex=["A", "B", "C", "D", "E"])

    with pytest.raises(Exception) as exc_info:
        df[""]

    exception_raised = exc_info.value

    assert exception_raised
