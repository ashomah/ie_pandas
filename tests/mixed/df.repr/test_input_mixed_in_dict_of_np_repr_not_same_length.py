from ie_pandas import DataFrame
import pytest
import numpy as np


def test_input_mixed_in_dict_of_np_repr_not_same_length():
    obj = {"age": np.array([30, 53, 31, 47, 32]), "albums": np.array([4, 10])}

    with pytest.raises(Exception) as exc_info:
        df = DataFrame(obj)

    exception_raised = exc_info.value

    assert exception_raised
