from ie_pandas import DataFrame
import numpy as np
import pytest

def test_bool_input_in_dict_of_np_array():
    artists_dict_of_lists = [[True, False, True], [False, True, False]]
    np_array = np.array(artists_dict_of_lists)
    dict_of_lists_df = DataFrame(np_array, colindex=['age', 'albums'])

    expected_output ="     age  albums\n0   True   False\n1  False    True\n2   True   False"

    actual_output = repr(dict_of_lists_df)

    assert actual_output == expected_output