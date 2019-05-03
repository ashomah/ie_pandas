from ie_pandas import DataFrame
import pytest
import numpy as np

def test_input_mixed_in_np_get_row_by_index():
    obj = np.array([30, 53.0, '31', True, 32])
    df = DataFrame(obj, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    expected_output = ['53.0']

    actual_output = df.get_row(1)

    assert actual_output == expected_output

def test_input_mixed_in_np_get_row_by_rowindex():
    obj = np.array([30, 53.0, '31', True, 32])
    df = DataFrame(obj, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    expected_output = ['53.0']

    actual_output = df.get_row('B')

    assert actual_output == expected_output

def test_input_mixed_in_np_get_row_wrong():
    obj = np.array([30, 53.0, '31', True, 32])
    df = DataFrame(obj, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    with pytest.raises(Exception) as exc_info:
        df.get_row(100)

    exception_raised = exc_info.value

    assert exception_raised

def test_input_mixed_in_np_get_row_empty():
    obj = np.array([30, 53.0, '31', True, 32])
    df = DataFrame(obj, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    with pytest.raises(TypeError) as exc_info:
        df.get_row()

    exception_raised = exc_info.value

    assert exception_raised

def test_input_mixed_in_np_get_row_imaginary():
    obj = np.array([30, 53.0, '31', True, 32])
    df = DataFrame(obj, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    with pytest.raises(Exception) as exc_info:
        df.get_row(1+2j)

    exception_raised = exc_info.value

    assert exception_raised

