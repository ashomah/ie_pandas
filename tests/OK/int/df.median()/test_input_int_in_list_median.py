from ie_pandas import DataFrame
import pytest

def test_input_int_in_list_median_odd():
    artists_age_list = [30, 53, 31, 47, 32]
    df = DataFrame(artists_age_list, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E'])

    expected_output = [32.0]

    actual_output = df.median()

    assert actual_output == expected_output

def test_input_int_in_list_median_even():
    artists_age_list = [30, 53, 31, 47, 32, 100]
    df = DataFrame(artists_age_list, colindex = ['AGE'], rowindex = ['A', 'B', 'C', 'D', 'E', 'F'])

    expected_output = [39.5]

    actual_output = df.median()

    assert actual_output == expected_output