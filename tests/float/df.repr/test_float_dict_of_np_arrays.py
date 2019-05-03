from ie_pandas import DataFrame
import pytest
import numpy as np


def float_input_in_dict_of_lists():
    artists_dict_of_lists = [
        np.array([30.0, 53.0, 31.0, 47.0, 32.0]),
        np.array([4.0, 10.0, 2.0, 5.0, 4.0]),
    ]
    dict_of_lists_df = DataFrame(artists_dict_of_lists, colindex=["age", "albums"])

    expected_output = (
        "    age  albums"
        + "/n"
        + "0  30.0     4.0"
        + "/n"
        + "1  53.0    10.0"
        + "/n"
        + "2  31.0     2.0"
        + "/n"
        + "3  47.0     5.0"
        + "/n"
        + "4  32.0     4.0"
    )

    actual_output = rper(dict_of_lists_df)

    assert actual_output == expected_output
