from ie_pandas import DataFrame
import pytest


def test_string_input_in_list_of_lists():
    obj = [
        ["Björk", "Chris", "Solange"],
        ["James Blake", "DJ Koze", "David Byrne"],
    ]
    df = DataFrame(obj)

    expected_output = (
        "         0            1"
        + "\n"
        + "0    Björk  James Blake"
        + "\n"
        + "1    Chris      DJ Koze"
        + "\n"
        + "2  Solange  David Byrne"
    )

    actual_output = repr(df)

    assert actual_output == expected_output
