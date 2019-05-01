from ie_pandas import DataFrame
import pytest

def test_input_int_in_list_print_row_index():
    artists_age_list = [30, 53, 31, 47, 32]
    df = DataFrame(artists_age_list, rowindex = ['A', 'B', 'C', 'D', 'E'])

    expected_output =  "    0" + "\n" + \
                       "A  30" + "\n" + \
                       "B  53" + "\n" + \
                       "C  31" + "\n" + \
                       "D  47" + "\n" + \
                       "E  32"

    actual_output = repr(df)

    assert actual_output == expected_output