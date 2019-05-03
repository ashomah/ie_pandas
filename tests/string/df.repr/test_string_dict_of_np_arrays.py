from ie_pandas import DataFrame
import pytest
import numpy as np


def test_string_input_in_dict_of_np():
    artists_dict_of_np = {
        "f_name": np.array(["Björk", "Chris", "Solange"]),
        "m_name": np.array(["James Blake", "DJ Koze", "David Byrne"]),
    }
    dict_of_np_df = DataFrame(artists_dict_of_np)

    expected_output = (
        "    f_name       m_name"
        + "\n"
        + "0    Björk  James Blake"
        + "\n"
        + "1    Chris      DJ Koze"
        + "\n"
        + "2  Solange  David Byrne"
    )

    actual_output = repr(dict_of_np_df)

    assert actual_output == expected_output
