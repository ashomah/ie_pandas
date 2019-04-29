from ie_pandas import DataFrame
import pytest

def bool_input_in_dict_of_lists():
    artists_dict_of_lists = [[True, False, True, False, True], [False, True, False, True, False]]
    np_array = np.array(artists_dict_of_lists)
    dict_of_lists_df = DataFrame(np_array, colindex=['age', 'albums'])

    expected_output =       age   albums
0    True   False
1    False  True
2    True   False
3    False  True
4    True   False

    actual_output = DataFrame(dict_of_lists_df)

    assert actual_output == expected_output