from ie_pandas import DataFrame
import pytest

def test_input_int_in_list_colindex_both_index_axis():
    artists_age_list = [30, 53, 31, 47, 32]
    df = DataFrame(artists_age_list, rowindex = ['AGE'], colindex = ['A', 'B', 'C', 'D', 'E'], axis=1)

    expected_output = ['A', 'B', 'C', 'D', 'E']

    actual_output = df.colindex

    assert actual_output == expected_output