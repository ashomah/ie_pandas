from ie_pandas import DataFrame
import pytest


def test_input_int_in_list_of_lists_repr_wrong_row_index():
    obj = [[30, 53, 31, 47, 32], [4, 10, 2, 5, 4]]

    with pytest.raises(Exception) as exc_info:
        df = DataFrame(obj, rowindex=["A", "B", "C", "D", "E", "TOOMANY"])

    exception_raised = exc_info.value

    assert exception_raised
