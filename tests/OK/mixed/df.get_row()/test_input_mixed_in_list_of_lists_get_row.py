from ie_pandas import DataFrame
import pytest

def test_input_mixed_in_list_of_lists_get_row_by_index():
    obj = [[30.1, 53.1, 31.1, 47.1, 32.1], [4, 10, 2, 5, 4], ['a', 'b', 'c', 'd', 'e'], [True, False, True, True, False]]
    df = DataFrame(obj, colindex = ['AGE', 'ALBUMS', 'C', 'D'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    expected_output = [53.1, 10, 'b', False]

    actual_output = df.get_row(1)

    assert actual_output == expected_output

def test_input_mixed_in_list_of_lists_get_row_by_rowindex():
    obj = [[30.1, 53.1, 31.1, 47.1, 32.1], [4, 10, 2, 5, 4], ['a', 'b', 'c', 'd', 'e'], [True, False, True, True, False]]
    df = DataFrame(obj, colindex = ['AGE', 'ALBUMS', 'C', 'D'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    expected_output = [53.1, 10, 'b', False]
    
    actual_output = df.get_row('B')

    assert actual_output == expected_output

def test_input_mixed_in_list_of_lists_get_row_wrong():
    obj = [[30.1, 53.1, 31.1, 47.1, 32.1], [4, 10, 2, 5, 4], ['a', 'b', 'c', 'd', 'e'], [True, False, True, True, False]]
    df = DataFrame(obj, colindex = ['AGE', 'ALBUMS', 'C', 'D'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    with pytest.raises(Exception) as exc_info:
        df.get_row(100)

    exception_raised = exc_info.value

    assert exception_raised

def test_input_mixed_in_list_of_lists_get_row_empty():
    obj = [[30.1, 53.1, 31.1, 47.1, 32.1], [4, 10, 2, 5, 4], ['a', 'b', 'c', 'd', 'e'], [True, False, True, True, False]]
    df = DataFrame(obj, colindex = ['AGE', 'ALBUMS', 'C', 'D'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    with pytest.raises(TypeError) as exc_info:
        df.get_row()

    exception_raised = exc_info.value

    assert exception_raised

def test_input_mixed_in_list_of_lists_get_row_imaginary():
    obj = [[30.1, 53.1, 31.1, 47.1, 32.1], [4, 10, 2, 5, 4], ['a', 'b', 'c', 'd', 'e'], [True, False, True, True, False]]
    df = DataFrame(obj, colindex = ['AGE', 'ALBUMS', 'C', 'D'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    with pytest.raises(Exception) as exc_info:
        df.get_row(1+2j)

    exception_raised = exc_info.value

    assert exception_raised

