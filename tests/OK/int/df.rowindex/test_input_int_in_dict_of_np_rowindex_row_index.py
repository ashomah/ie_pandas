from ie_pandas import DataFrame
import pytest
import numpy as np

def test_input_int_in_dict_of_np_rowindex_row_index():
    artists_dict_of_lists = {'age':np.array([30, 53, 31, 47, 32]), 'albums':np.array([4, 10, 2, 5, 4])}
    dict_of_lists_df = DataFrame(artists_dict_of_lists, rowindex = ['A', 'B', 'C', 'D', 'E'])

    expected_output =  ['A', 'B', 'C', 'D', 'E']

    actual_output = dict_of_lists_df.rowindex

    assert actual_output == expected_output