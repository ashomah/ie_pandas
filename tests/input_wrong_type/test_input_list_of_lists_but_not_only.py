from ie_pandas import DataFrame
import pytest

def test_input_list_of_lists_but_not_only():

    with pytest.raises(Exception) as exc_info:
        DataFrame([[1, 2, 3, 4],[1, 2, 3, 4], 1])

    exception_raised = exc_info.value

    assert exception_raised