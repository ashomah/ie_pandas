from ie_pandas import DataFrame
import pytest

def test_string_input_in_list():
    artists_age_list = ["James Blake", "Björk", "Christine & The Queens", "DJ Koze", "Solange"]

    df1 = DataFrame(artists_age_list)

    expected_output = "                        0\n0             James Blake\n1                   Björk\n2  Christine & The Queens\n3                 DJ Koze\n4                 Solange"
    
    actual_output = repr(df1)

    assert actual_output == expected_output