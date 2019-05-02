from ie_pandas import DataFrame
import pytest

def test_input_mixed_in_list_of_lists_repr_wrong_row_index():
    obj = [[30.1, 53.1, 31.1, 47.1, 32.1], [4, 10, 2, 5, 4], ['a', 'b', 'c', 'd', 'e'], [True, False, True, True, False]]

    with pytest.raises(Exception) as exc_info:
        df = DataFrame(obj, rowindex = ['A', 'B', 'C', 'D', 'E', 'TOOMANY'])

    exception_raised = exc_info.value

    assert exception_raised