from ie_pandas import DataFrame
import pytest

def bool_input_in_dict_of_lists():
    artists_dict_of_lists = {'age':[True, False, True, False, True], 'albums':[False, True, False, True, False]}
    dict_of_lists_df = DataFrame(artists_dict_of_lists, rowindex = ['R1', 'R2', 'R3', 'R4', 'R5'], colindex=['age', 'albums'])

    expected_output =       age   albums
R1    True   False
R2    False  True
R3    True   False
R4    False  True
R5    True   False

    actual_output = DataFrame(dict_of_lists_df)

    assert actual_output == expected_output