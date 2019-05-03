from ie_pandas import DataFrame
import pytest


def test_input_mixed_in_list_rowindex_row_index():
    obj = [30, 53.0, "31", True, 32]

    with pytest.raises(Exception) as exc_info:
        df = DataFrame(obj, rowindex=["A", "B", "C", "D", "E"])

    exception_raised = exc_info.value

    assert exception_raised
