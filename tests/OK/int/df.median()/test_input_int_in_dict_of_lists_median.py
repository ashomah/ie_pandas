from ie_pandas import DataFrame
import pytest

def test_input_int_in_dict_of_lists_median_odd():
    artists_dict_of_lists = {'age':[30, 53, 31, 47, 32], 'albums':[4, 10, 2, 5, 4]}
    dict_of_lists_df = DataFrame(artists_dict_of_lists, colindex = ['AGE', 'ALBUMS'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    expected_output = [32.0, 4.0]

    actual_output = dict_of_lists_df.median()

    assert actual_output == expected_output

def test_input_int_in_dict_of_lists_median_even():
    artists_dict_of_lists = {'age':[30, 53, 31, 47, 32, 100], 'albums':[4, 10, 2, 5, 4, 100]}
    dict_of_lists_df = DataFrame(artists_dict_of_lists, colindex = ['AGE', 'ALBUMS'], rowindex = ['A', 'B', 'C', 'D', 'E', 'F'])

    expected_output = [39.5, 4.5]

    actual_output = dict_of_lists_df.median()

    assert actual_output == expected_output