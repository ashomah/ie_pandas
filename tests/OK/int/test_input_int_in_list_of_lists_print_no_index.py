from ie_pandas import DataFrame
import pytest

def test_input_int_in_list_of_lists_print_no_index():
    obj = [[30, 53, 31, 47, 32], [4, 10, 2, 5, 4]]
    df = DataFrame(obj)

    expected_output =  "    0   1" + "\n" + \
                       "0  30   4" + "\n" + \
                       "1  53  10" + "\n" + \
                       "2  31   2" + "\n" + \
                       "3  47   5" + "\n" + \
                       "4  32   4"

    actual_output = repr(df)

    assert actual_output == expected_output