from ie_pandas.DataFrame import DataFrame
import pytest


def test_min_values_dataframe():
    artists_dict = {"artist_name": ["James Blake", "Björk", "Christine & The Queens", "DJ Koze", "Solange"], "age": [30, 53, 31, 47, 32], "albums": [4, 10, 2, 5, 4]}

    df1 = DataFrame(artists_dict)

    expected_output = [{'age': 30, 'albums': 2}]

    actual_output = df1.min()

    assert actual_output == expected_output