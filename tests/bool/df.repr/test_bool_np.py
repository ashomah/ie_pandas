from ie_pandas import DataFrame
import pytest
import numpy as np

def test_bool_input_in_np():
    artists_age_list = np.array([True, False, True, False, True])
    
    df1 = DataFrame(artists_age_list, axis = 1)

    expected_output ="      0      1     2      3     4\n0  True  False  True  False  True"

    actual_output = repr(df1)

    assert actual_output == expected_output