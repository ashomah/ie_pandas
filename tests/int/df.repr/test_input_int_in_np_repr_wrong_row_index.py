from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_int_in_list_repr_wrong_row_index():
    obj = np.array([30, 53, 31, 47, 32])

    with pytest.raises(Exception) as exc_info:
        df = DataFrame(obj, rowindex=["A", "B", "C", "D", "E", "TOOMANY"])

    exception_raised = exc_info.value

    assert exception_raised
