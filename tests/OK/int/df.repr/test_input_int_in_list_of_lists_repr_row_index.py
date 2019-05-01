from ie_pandas import DataFrame
import pytest

def test_input_int_in_list_of_lists_repr_row_index():
    obj = [[30, 53, 31, 47, 32], [4, 10, 2, 5, 4]]
    df = DataFrame(obj, rowindex = ['A', 'B', 'C', 'D', 'E'])

    expected_output =  "    0   1" + "\n" + \
                       "A  30   4" + "\n" + \
                       "B  53  10" + "\n" + \
                       "C  31   2" + "\n" + \
                       "D  47   5" + "\n" + \
                       "E  32   4"

    actual_output = repr(df)

    assert actual_output == expected_output