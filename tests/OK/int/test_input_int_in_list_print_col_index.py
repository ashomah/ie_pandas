from ie_pandas import DataFrame
import pytest

def test_input_int_in_list_print_col_index():
    artists_age_list = [30, 53, 31, 47, 32]
    df = DataFrame(artists_age_list, colindex = ['AGE'])

    expected_output =  "   AGE" + "\n" + \
                       "0   30" + "\n" + \
                       "1   53" + "\n" + \
                       "2   31" + "\n" + \
                       "3   47" + "\n" + \
                       "4   32"

    actual_output = repr(df)

    assert actual_output == expected_output