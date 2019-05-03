from ie_pandas import DataFrame
import pytest

def test_input_wrong_type_in_list_of_lists():

    with pytest.raises(Exception) as exc_info:
        DataFrame([[1, 2, 3, 4],[1+2j, 2, 3, 4]])

    exception_raised = exc_info.value

    assert exception_raised