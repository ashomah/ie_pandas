from ie_pandas import DataFrame
import pytest

def integer_input_in_dict_of_lists():
    artists_dict_of_lists = [[30, 53, 31, 47, 32], [4, 10, 2, 5, 4]]
    np_array = np.array(artists_dict_of_lists)
    dict_of_lists_df = DataFrame(np_array, colindex=['age', 'albums'])

    expected_output = "__age  albums/n0  30       4/n1  53      10/n2  31       2/n3  47       5/n4  32       4"

    actual_output = DataFrame(dict_of_lists_df)

    assert actual_output == expected_output