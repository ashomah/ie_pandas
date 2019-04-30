from ie_pandas import DataFrame
import pytest

def float_input_in_dict_of_lists():
    artists_dict_of_lists = [[30.0, 53.0, 31.0, 47.0, 32.0], [4.0, 10.0, 2.0, 5.0, 4.0]]
    np_array = np.array(artists_dict_of_lists)
    dict_of_lists_df = DataFrame(np_array, colindex=['age', 'albums'])

    expected_output = "__age  albums/n0  30.0       4.0/n1  53.0      10.0/n2  31.0       2.0/n3  47.0       5.0/n4  32.0       4.0"


    actual_output = DataFrame(dict_of_lists_df)

    assert actual_output == expected_output