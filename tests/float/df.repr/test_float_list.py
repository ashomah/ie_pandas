from ie_pandas import DataFrame
import pytest


def float_input_in_list():
    artists_age_list = [30.0, 53.0, 31.0, 47.0, 32.0]
    df1 = DataFrame(artists_age_list)

    expected_output = (
        "      0"
        + "\n"
        + "0  30.0"
        + "\n"
        + "1  53.0"
        + "\n"
        + "2  31.0"
        + "\n"
        + "3  47.0"
        + "\n"
        + "4  32.0"
    )

    actual_output = repr(df1)

    assert actual_output == expected_output
