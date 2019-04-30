from ie_pandas import DataFrame
import pytest

def float_input_in_dict_of_lists():
    artists_dict_of_lists = {'age':[30.0, 53.0, 31.0, 47.0, 32.0], 'albums':[4.0, 10.0, 2.0, 5.0, 4.0]}
    dict_of_lists_df = DataFrame(artists_dict_of_lists, rowindex = ['R1', 'R2', 'R3', 'R4', 'R5'], colindex=['age', 'albums'])

    expected_output = "__age  albums/nR1  30.0       4.0/nR2  53.0      10.0/nR3  31.0       2.0/nR4  47.0       5.0/nR5  32.0       4.0"


    actual_output = DataFrame(dict_of_lists_df)

    assert actual_output == expected_output