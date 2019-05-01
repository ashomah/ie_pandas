from ie_pandas import DataFrame
import pytest

def test_input_int_in_list_rowindex_no_index():
    artists_age_list = [30, 53, 31, 47, 32]
    df = DataFrame(artists_age_list)

    expected_output =  ['0', '1', '2', '3', '4']

    actual_output = df.rowindex

    assert actual_output == expected_output