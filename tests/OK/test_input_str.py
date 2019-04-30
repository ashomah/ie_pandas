from ie_pandas import DataFrame
import pytest

def test_input_str():

    with pytest.raises(Exception) as exc_info:
        DataFrame('e')

    exception_raised = exc_info.value

    assert exception_raised