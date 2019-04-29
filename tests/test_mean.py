from ie_pandas.DataFrame import DataFrame
import pytest


def test_calculate_mean_values_in_dataframe():
    artists_dict = {"artist_name": ["James Blake", "Björk", "Christine & The Queens", "DJ Koze", "Solange"], "age": [30, 53, 31, 47, 32], "albums": [4, 10, 2, 5, 4]}

    df1 = DataFrame(artists_dict)

    expected_output = age: 38.6, albums: 5

    actual_output = df1.mean()

    assert actual_output == expected_output