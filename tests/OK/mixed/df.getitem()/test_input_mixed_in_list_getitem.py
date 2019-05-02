from ie_pandas import DataFrame
import pytest
import numpy as np

def test_input_mixed_in_list_getitem_by_index():
    obj = [30, 53.0, '31', True, 32]
    
    with pytest.raises(Exception) as exc_info:
        df = DataFrame(obj, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    exception_raised = exc_info.value

    assert exception_raised

def test_input_mixed_in_list_getitem_by_rowindex():
    obj = [30, 53.0, '31', True, 32]

    with pytest.raises(Exception) as exc_info:
        df = DataFrame(obj, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    exception_raised = exc_info.value

    assert exception_raised

def test_input_mixed_in_list_getitem_wrong():
    obj = [30, 53.0, '31', True, 32]

    with pytest.raises(Exception) as exc_info:
        df[100]

    exception_raised = exc_info.value

    assert exception_raised

def test_input_mixed_in_list_getitem_empty():
    obj = [30, 53.0, '31', True, 32]

    with pytest.raises(Exception) as exc_info:
        df['']

    exception_raised = exc_info.value

    assert exception_raised
