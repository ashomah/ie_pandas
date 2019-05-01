from ie_pandas import DataFrame
import pytest
import numpy as np

def test_input_int_in_dict_of_np_repr_wrong_col_index():
    artists_dict_of_lists = {'age':np.array([30, 53, 31, 47, 32]), 'albums':np.array([4, 10, 2, 5, 4])}

    with pytest.raises(Exception) as exc_info:
        dict_of_lists_df = DataFrame(artists_dict_of_lists, colindex = ['AGE', 'ALBUMS', 'TOOMANY'])

    exception_raised = exc_info.value

    assert exception_raised
