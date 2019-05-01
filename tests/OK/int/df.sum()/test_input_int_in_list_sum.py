from ie_pandas import DataFrame
import pytest

def test_input_int_in_list_sum():
    artists_age_list = [30, 53, 31, 47, 32]
    df = DataFrame(artists_age_list, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    expected_output = [193]

    actual_output = df.sum()

    assert actual_output == expected_output