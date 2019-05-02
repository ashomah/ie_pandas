from ie_pandas import DataFrame
import pytest

def test_input_int_in_list_get_row_by_index():
    obj = [30, 53, 31, 47, 32]
    df = DataFrame(obj, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    expected_output = [53]

    actual_output = df.get_row(1)

    assert actual_output == expected_output

def test_input_int_in_list_get_row_by_rowindex():
    obj = [30, 53, 31, 47, 32]
    df = DataFrame(obj, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    expected_output = [53]
    
    actual_output = df.get_row('B')

    assert actual_output == expected_output

def test_input_int_in_list_get_row_wrong():
    obj = [30, 53, 31, 47, 32]
    df = DataFrame(obj, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    with pytest.raises(Exception) as exc_info:
        df.get_row(100)

    exception_raised = exc_info.value

    assert exception_raised

def test_input_int_in_list_get_row_empty():
    obj = [30, 53, 31, 47, 32]
    df = DataFrame(obj, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    with pytest.raises(TypeError) as exc_info:
        df.get_row()

    exception_raised = exc_info.value

    assert exception_raised
