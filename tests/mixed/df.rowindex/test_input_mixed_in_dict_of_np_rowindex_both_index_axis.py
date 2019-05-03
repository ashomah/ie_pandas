from ie_pandas import DataFrame
import pytest
import numpy as np

def test_input_mixed_in_dict_of_np_rowindex_both_index_axis():
    obj = {'age':np.array([30.1, 53.1, 31.1, 47.1, 32.1]), 'albums':np.array([4, 10, 2, 5, 4]), 'C':np.array(['a', 'b', 'c', 'd', 'e']), 'D':np.array([True, False, True, True, False])}

    with pytest.raises(Exception) as exc_info:
        df = DataFrame(obj, rowindex = ['AGE', 'ALBUMS', 'C', 'D'], colindex = ['A', 'B', 'C', 'D', 'E'], axis=1)

    exception_raised = exc_info.value

    assert exception_raised
