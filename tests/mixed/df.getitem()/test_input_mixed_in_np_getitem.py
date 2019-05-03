from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_mixed_in_np_getitem_by_index():
    obj = np.array([30, 53.0, "31", True, 32])
    df = DataFrame(obj, colindex=["AGE"], rowindex=["A", "B", "C", "D", "E"])

    expected_output = np.array(["30", "53.0", "31", "True", "32"])

    actual_output = df[0]

    assert np.all(actual_output == expected_output)


def test_input_mixed_in_np_getitem_by_rowindex():
    obj = np.array([30, 53.0, "31", True, 32])
    df = DataFrame(obj, colindex=["AGE"], rowindex=["A", "B", "C", "D", "E"])

    expected_output = np.array(["30", "53.0", "31", "True", "32"])

    actual_output = df[0]

    assert np.all(actual_output == expected_output)


def test_input_mixed_in_np_getitem_wrong():
    obj = np.array([30, 53.0, "31", True, 32])

    with pytest.raises(Exception) as exc_info:
        df[100]

    exception_raised = exc_info.value

    assert exception_raised


def test_input_mixed_in_np_getitem_empty():
    obj = np.array([30, 53.0, "31", True, 32])

    with pytest.raises(Exception) as exc_info:
        df[""]

    exception_raised = exc_info.value

    assert exception_raised
