from ie_pandas import DataFrame
import pytest

def test_input_int_in_list_df_row_index():
    obj = [30, 53, 31, 47, 32]
    df = DataFrame(obj, rowindex = ['A', 'B', 'C', 'D', 'E'])

    expected_output =  {'0': [30, 53, 31, 47, 32]}

    actual_output = df.df

    assert actual_output == expected_output