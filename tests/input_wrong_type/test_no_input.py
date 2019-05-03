from ie_pandas import DataFrame
import pytest


def test_no_input():

    with pytest.raises(TypeError) as exc_info:
        DataFrame()

    exception_raised = exc_info.value

    assert exception_raised
