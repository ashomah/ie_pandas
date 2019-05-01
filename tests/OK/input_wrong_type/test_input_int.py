from ie_pandas import DataFrame
import pytest

def test_input_int():

    with pytest.raises(Exception) as exc_info:
        DataFrame(10)

    exception_raised = exc_info.value

    assert exception_raised