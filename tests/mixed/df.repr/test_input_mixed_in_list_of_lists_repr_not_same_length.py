from ie_pandas import DataFrame
import pytest

def test_input_mixed_in_list_of_lists_repr_not_same_length():
    obj = [[30, 53, 31, 47, 32], [4, 10]]

    with pytest.raises(Exception) as exc_info:
        df = DataFrame(obj)

    exception_raised = exc_info.value

    assert exception_raised
