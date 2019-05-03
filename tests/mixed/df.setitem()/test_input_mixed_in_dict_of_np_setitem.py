from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_mixed_in_dict_of_np_setitem_by_index():
    obj = {
        "age": np.array([30.1, 53.1, 31.1, 47.1, 32.1]),
        "albums": np.array([4, 10, 2, 5, 4]),
        "C": np.array(["a", "b", "c", "d", "e"]),
        "D": np.array([True, False, True, True, False]),
    }
    df = DataFrame(
        obj, colindex=["AGE", "ALBUMS", "C", "D"], rowindex=["A", "B", "C", "D", "E"]
    )
    df[0] = [100, 100, 100, 100, 100]

    expected_output = np.array([100, 100, 100, 100, 100])

    actual_output = df[0]

    assert np.all(actual_output == expected_output)


def test_input_mixed_in_dict_of_np_setitem_by_rowindex():
    obj = {
        "age": np.array([30.1, 53.1, 31.1, 47.1, 32.1]),
        "albums": np.array([4, 10, 2, 5, 4]),
        "C": np.array(["a", "b", "c", "d", "e"]),
        "D": np.array([True, False, True, True, False]),
    }
    df = DataFrame(
        obj, colindex=["AGE", "ALBUMS", "C", "D"], rowindex=["A", "B", "C", "D", "E"]
    )
    df["AGE"] = [100, 100, 100, 100, 100]

    expected_output = np.array([100, 100, 100, 100, 100])

    actual_output = df["AGE"]

    assert np.all(actual_output == expected_output)


def test_input_mixed_in_dict_of_np_setitem_wrong():
    obj = {
        "age": np.array([30.1, 53.1, 31.1, 47.1, 32.1]),
        "albums": np.array([4, 10, 2, 5, 4]),
        "C": np.array(["a", "b", "c", "d", "e"]),
        "D": np.array([True, False, True, True, False]),
    }
    df = DataFrame(
        obj, colindex=["AGE", "ALBUMS", "C", "D"], rowindex=["A", "B", "C", "D", "E"]
    )

    with pytest.raises(Exception) as exc_info:
        df[100] = [100, 100, 100, 100, 100]

    exception_raised = exc_info.value

    assert exception_raised


def test_input_mixed_in_dict_of_np_setitem_empty():
    obj = {
        "age": np.array([30.1, 53.1, 31.1, 47.1, 32.1]),
        "albums": np.array([4, 10, 2, 5, 4]),
        "C": np.array(["a", "b", "c", "d", "e"]),
        "D": np.array([True, False, True, True, False]),
    }
    df = DataFrame(
        obj, colindex=["AGE", "ALBUMS", "C", "D"], rowindex=["A", "B", "C", "D", "E"]
    )

    with pytest.raises(Exception) as exc_info:
        df[""] = [100, 100, 100, 100, 100]

    exception_raised = exc_info.value

    assert exception_raised


def test_input_mixed_in_dict_of_np_setitem_wrong_length():
    obj = {
        "age": np.array([30.1, 53.1, 31.1, 47.1, 32.1]),
        "albums": np.array([4, 10, 2, 5, 4]),
        "C": np.array(["a", "b", "c", "d", "e"]),
        "D": np.array([True, False, True, True, False]),
    }
    df = DataFrame(
        obj, colindex=["AGE", "ALBUMS", "C", "D"], rowindex=["A", "B", "C", "D", "E"]
    )

    with pytest.raises(Exception) as exc_info:
        df[0] = [100]

    exception_raised = exc_info.value

    assert exception_raised


def test_input_mixed_in_dict_of_np_setitem_wrong_length_rowindex():
    obj = {
        "age": np.array([30.1, 53.1, 31.1, 47.1, 32.1]),
        "albums": np.array([4, 10, 2, 5, 4]),
        "C": np.array(["a", "b", "c", "d", "e"]),
        "D": np.array([True, False, True, True, False]),
    }
    df = DataFrame(
        obj, colindex=["AGE", "ALBUMS", "C", "D"], rowindex=["A", "B", "C", "D", "E"]
    )

    with pytest.raises(Exception) as exc_info:
        df["AGE"] = [100]

    exception_raised = exc_info.value

    assert exception_raised


def test_input_mixed_in_dict_of_np_setitem_inconsistent_type():
    obj = {
        "age": np.array([30.1, 53.1, 31.1, 47.1, 32.1]),
        "albums": np.array([4, 10, 2, 5, 4]),
        "C": np.array(["a", "b", "c", "d", "e"]),
        "D": np.array([True, False, True, True, False]),
    }
    df = DataFrame(
        obj, colindex=["AGE", "ALBUMS", "C", "D"], rowindex=["A", "B", "C", "D", "E"]
    )

    with pytest.raises(Exception) as exc_info:
        df[0] = [100, 100, "100", 100.0, 100]

    exception_raised = exc_info.value

    assert exception_raised
