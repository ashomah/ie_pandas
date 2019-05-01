from ie_pandas import DataFrame
import pytest

def test_input_int_in_dict_of_lists_df_both_index():
    artists_dict_of_lists = {'age':[30, 53, 31, 47, 32], 'albums':[4, 10, 2, 5, 4]}
    dict_of_lists_df = DataFrame(artists_dict_of_lists, colindex = ['AGE', 'ALBUMS'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    expected_output = {'AGE': [30, 53, 31, 47, 32], 'ALBUMS': [4, 10, 2, 5, 4]}

    actual_output = dict_of_lists_df.df

    assert actual_output == expected_output