from ie_pandas import DataFrame
import pytest

def test_float_input_list_of_lists():
    obj = [[3.0, 2.0], ['as', 'bs'], [2, 1], [True, True]]
    df1 = DataFrame(obj)
    
    expected_output = "     0   1  2     3" + "\n" + \
                      "0  3.0  as  2  True" + "\n" + \
                      "1  2.0  bs  1  True"
    
    actual_output = repr(df1)
    
    assert actual_output == expected_output