from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_bool_in_np_get_row_by_index():
    obj = np.array([False, True, False])

    df = DataFrame(obj, colindex=["AGE"], rowindex=["A", "B", "C"])

    expected_output = [True]

    actual_output = df.get_row(1)

    assert actual_output == expected_output


def test_input_bool_in_np_get_row_by_rowindex():
    obj = np.array([False, True, False])
    
    df = DataFrame(obj, colindex=["AGE"], rowindex=["A", "B", "C"])

    expected_output = [True]

    actual_output = df.get_row("B")

    assert actual_output == expected_output


def test_input_bool_in_np_get_row_wrong():
    obj = np.array([False, True, False])
    
    df = DataFrame(obj, colindex=["AGE"], rowindex=["A", "B", "C"])

    expected_output = [True]
    with pytest.raises(Exception) as exc_info:
        df.get_row(100)

    exception_raised = exc_info.value

    assert exception_raised


def test_input_bool_in_np_get_row_empty():
    obj = np.array([False, True, False])
    
    df = DataFrame(obj, colindex=["AGE"], rowindex=["A", "B", "C"])

    expected_output = [True]
    with pytest.raises(TypeError) as exc_info:
        df.get_row()

    exception_raised = exc_info.value

    assert exception_raised


def test_input_bool_in_np_get_row_imaginary():
    obj = np.array([False, True, False])
    
    df = DataFrame(obj, colindex=["AGE"], rowindex=["A", "B", "C"])

    expected_output = [True]
    with pytest.raises(Exception) as exc_info:
        df.get_row(1 + 2j)

    exception_raised = exc_info.value

    assert exception_raised
