from ie_pandas import DataFrame
import pytest

def test_input_int_in_dict_of_lists_repr_col_index():
    artists_dict_of_lists = {'age':[30, 53, 31, 47, 32], 'albums':[4, 10, 2, 5, 4]}
    dict_of_lists_df = DataFrame(artists_dict_of_lists, colindex = ['AGE', 'ALBUMS'])

    expected_output =  "   AGE  ALBUMS" + "\n" + \
                       "0   30       4" + "\n" + \
                       "1   53      10" + "\n" + \
                       "2   31       2" + "\n" + \
                       "3   47       5" + "\n" + \
                       "4   32       4"

    actual_output = repr(dict_of_lists_df)

    assert actual_output == expected_output