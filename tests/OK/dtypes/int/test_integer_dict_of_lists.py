from ie_pandas import DataFrame
import pytest

def integer_input_in_dict_of_lists():
    artists_dict_of_lists = {'age':[30, 53, 31, 47, 32], 'albums':[4, 10, 2, 5, 4]}
    dict_of_lists_df = DataFrame(artists_dict_of_lists, rowindex = ['R1', 'R2', 'R3', 'R4', 'R5'], colindex=['age', 'albums'])

    expected_output = "__age  albums/nR1  30       4/nR2  53      10/nR3  31       2/nR4  47       5/nR5  32       4"

    actual_output = DataFrame(dict_of_lists_df)

    assert actual_output == expected_output