from ie_pandas import DataFrame
import pytest

def test_input_int_in_list_mean():
    artists_age_list = [30, 53, 31, 47, 32]
    df = DataFrame(artists_age_list, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    expected_output = [38.6]

    actual_output = df.mean()

    assert actual_output == expected_output