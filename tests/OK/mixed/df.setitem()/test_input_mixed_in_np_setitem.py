from ie_pandas import DataFrame
import pytest
import numpy as np

def test_input_mixed_in_np_setitem_by_index():
    obj = np.array([30, 53.0, '31', True, 32])
    df = DataFrame(obj, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])
    df[0] = [100, 100, 100, 100, 100]

    expected_output = np.array([100, 100, 100, 100, 100])

    actual_output = df[0]

    assert np.all(actual_output == expected_output)

def test_input_mixed_in_np_setitem_by_rowindex():
    obj = np.array([30, 53.0, '31', True, 32])
    df = DataFrame(obj, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])
    df['AGE'] = [100, 100, 100, 100, 100]

    expected_output = np.array([100, 100, 100, 100, 100])
    
    actual_output = df['AGE']

    assert np.all(actual_output == expected_output)

def test_input_mixed_in_np_setitem_wrong():
    obj = np.array([30, 53.0, '31', True, 32])
    df = DataFrame(obj, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    with pytest.raises(Exception) as exc_info:
        df[100] = [100, 100, 100, 100, 100]

    exception_raised = exc_info.value

    assert exception_raised

def test_input_mixed_in_np_setitem_empty():
    obj = np.array([30, 53.0, '31', True, 32])
    df = DataFrame(obj, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    with pytest.raises(Exception) as exc_info:
        df[''] = [100, 100, 100, 100, 100]

    exception_raised = exc_info.value

    assert exception_raised

def test_input_mixed_in_np_setitem_wrong_length():
    obj = np.array([30, 53.0, '31', True, 32])
    df = DataFrame(obj, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    with pytest.raises(Exception) as exc_info:
        df[0] = [100]

    exception_raised = exc_info.value

    assert exception_raised

def test_input_mixed_in_np_setitem_wrong_length_rowindex():
    obj = np.array([30, 53.0, '31', True, 32])
    df = DataFrame(obj, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    with pytest.raises(Exception) as exc_info:
        df['AGE'] = [100]

    exception_raised = exc_info.value

    assert exception_raised

def test_input_mixed_in_np_setitem_inconsistent_type():
    obj = np.array([30, 53.0, '31', True, 32])
    df = DataFrame(obj, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    with pytest.raises(Exception) as exc_info:
        df[0] = [100, 100, '100', 100.0, 100]

    exception_raised = exc_info.value

    assert exception_raised
