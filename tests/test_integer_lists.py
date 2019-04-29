from ie_pandas import DataFrame

import pytest

def integer_input_in_list():
    artists_age_list = [30, 53, 31, 47, 32]

    df1 = DataFrame(artists_age_list)

    expected_output = [30, 53, 31, 47, 32]

    actual_output = DataFrame(df1)

    assert actual_output == expected_output