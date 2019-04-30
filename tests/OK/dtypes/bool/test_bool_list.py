from ie_pandas import DataFrame
import pytest

def bool_input_in_list():
    artists_age_list = [True, False, True, False, True]

    df1 = DataFrame(artists_age_list)

    expected_output = [True, False, True, False, True]

    actual_output = DataFrame(df1)

    assert actual_output == expected_output