from ie_pandas import DataFrame
import pytest
import numpy as np

def test_input_int_in_dict_of_np_min():
    artists_dict_of_lists = {'age':np.array([30, 53, 31, 47, 32]), 'albums':np.array([4, 10, 2, 5, 4])}
    dict_of_lists_df = DataFrame(artists_dict_of_lists, colindex = ['AGE', 'ALBUMS'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    expected_output = [30, 2]

    actual_output = dict_of_lists_df.min()

    assert actual_output == expected_output