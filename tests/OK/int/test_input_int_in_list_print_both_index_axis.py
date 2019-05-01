from ie_pandas import DataFrame
import pytest

def test_input_int_in_list_print_both_index_axis():
    artists_age_list = [30, 53, 31, 47, 32]
    df = DataFrame(artists_age_list, rowindex = ['AGE'], colindex = ['A', 'B', 'C', 'D', 'E'], axis=1)

    expected_output = "      A   B   C   D   E" + "\n" + \
                      "AGE  30  53  31  47  32"

    actual_output = repr(df)

    assert actual_output == expected_output