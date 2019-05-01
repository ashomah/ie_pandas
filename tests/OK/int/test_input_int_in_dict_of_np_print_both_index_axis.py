from ie_pandas import DataFrame
import pytest
import numpy as np

def test_input_int_in_dict_of_np_print_both_index_axis():
    artists_dict_of_lists = {'age':np.array([30, 53, 31, 47, 32]), 'albums':np.array([4, 10, 2, 5, 4])}
    dict_of_lists_df = DataFrame(artists_dict_of_lists, rowindex = ['AGE', 'ALBUMS'], colindex = ['A', 'B', 'C', 'D', 'E'], axis=1)

    expected_output = "         A   B   C   D   E" + "\n" + \
                      "AGE     30  53  31  47  32" + "\n" + \
                      "ALBUMS   4  10   2   5   4"

    actual_output = repr(dict_of_lists_df)

    assert actual_output == expected_output