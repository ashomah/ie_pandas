from ie_pandas import DataFrame
import pytest

def test_input_int_in_list_colindex_no_index():
    artists_age_list = [30, 53, 31, 47, 32]
    df = DataFrame(artists_age_list)

    expected_output =  ['0']

    actual_output = df.colindex

    assert actual_output == expected_output