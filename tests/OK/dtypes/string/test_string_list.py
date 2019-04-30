from ie_pandas import DataFrame
import pytest

def string_input_in_list():
    artists_age_list = ["James Blake", "Björk", "Christine & The Queens", "DJ Koze", "Solange"]

    df1 = DataFrame(artists_age_list)

    expected_output = ["James Blake", "Björk", "Christine & The Queens", "DJ Koze", "Solange"]

    actual_output = DataFrame(df1)

    assert actual_output == expected_output