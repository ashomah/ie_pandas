from ie_pandas import DataFrame
import pytest


def test_sum_values_in_dataframe():
    artists_dict = {"artist_name": ["James Blake", "Björk", "Christine & The Queens", "DJ Koze", "Solange"], "age": [30, 53, 31, 47, 32], "albums": [4, 10, 2, 5, 4]}

    df1 = DataFrame(artists_dict)

    expected_output = [193.0, 25.0]

    actual_output = df1.sum()

    assert actual_output == expected_output