from ie_pandas import DataFrame
import pytest

def float_input_in_list():
    artists_age_list = [30.0, 53.0, 31.0, 47.0, 32.0]

    df1 = DataFrame(artists_age_list)

    expected_output = [30.0, 53.0, 31.0, 47.0, 32.0]

    actual_output = DataFrame(df1)

    assert actual_output == expected_output