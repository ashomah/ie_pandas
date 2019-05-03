from ie_pandas import DataFrame
import pytest


def test_string_input_in_dict_of_lists():
    artists_dict_of_lists = {
        "f_name": ["Björk", "Chris", "Solange"],
        "m_name": ["James Blake", "DJ Koze", "David Byrne"],
    }
    dict_of_lists_df = DataFrame(artists_dict_of_lists)

    expected_output = (
        "    f_name       m_name"
        + "\n"
        + "0    Björk  James Blake"
        + "\n"
        + "1    Chris      DJ Koze"
        + "\n"
        + "2  Solange  David Byrne"
    )

    actual_output = repr(dict_of_lists_df)

    assert actual_output == expected_output
