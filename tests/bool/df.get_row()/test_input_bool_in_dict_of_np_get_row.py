from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_bool_in_dict_of_np_get_row_by_index():
    obj = {
        "A": np.array([False, False, False, True, False]),
        "B": np.array([True, False, True, True, False]),
    }

    df = DataFrame(
        obj,
        colindex=["A", "B"],
        rowindex=["a", "b", "c", "d", "e"],
    )

    expected_output = [False, False]

    actual_output = df.get_row(1)

    assert actual_output == expected_output


def test_input_bool_in_dict_of_np_get_row_by_rowindex():
    obj = {
        "A": np.array([False, False, False, True, False]),
        "B": np.array([True, False, True, True, False]),
    }

    df = DataFrame(
        obj,
        colindex=["A", "B"],
        rowindex=["a", "b", "c", "d", "e"],
    )

    expected_output = [False, False]

    actual_output = df.get_row("b")

    assert actual_output == expected_output


def test_input_bool_in_dict_of_np_get_row_wrong():
    obj = {
        "A": np.array([False, False, False, True, False]),
        "B": np.array([True, False, True, True, False]),
    }

    df = DataFrame(
        obj,
        colindex=["A", "B"],
        rowindex=["a", "b", "c", "d", "e"],
    )

    expected_output = [False, False]

    with pytest.raises(Exception) as exc_info:
        df.get_row(10)

    exception_raised = exc_info.value

    assert exception_raised


def test_input_bool_in_dict_of_np_get_row_empty():
    obj = {
        "A": np.array([False, False, False, True, False]),
        "B": np.array([True, False, True, True, False]),
    }

    df = DataFrame(
        obj,
        colindex=["A", "B"],
        rowindex=["a", "b", "c", "d", "e"],
    )

    expected_output = [False, False]

    with pytest.raises(TypeError) as exc_info:
        df.get_row()

    exception_raised = exc_info.value

    assert exception_raised


def test_input_bool_in_dict_of_np_get_row_imaginary():
    obj = {
        "A": np.array([False, False, False, True, False]),
        "B": np.array([True, False, True, True, False]),
    }
    
    df = DataFrame(
        obj,
        colindex=["A", "B"],
        rowindex=["a", "b", "c", "d", "e"],
    )

    expected_output = [False, False]

    with pytest.raises(Exception) as exc_info:
        df.get_row(1 + 2j)

    exception_raised = exc_info.value

    assert exception_raised
