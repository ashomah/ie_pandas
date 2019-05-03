from ie_pandas import DataFrame
import pytest
import numpy as np

def test_string_input_in_np():
    obj = np.array(["James Blake", "Björk", "Christine & The Queens", "DJ Koze", "Solange"])

    df1 = DataFrame(obj)

    expected_output = "                        0" + "\n" + \
                      "0             James Blake" + "\n" + \
                      "1                   Björk" + "\n" + \
                      "2  Christine & The Queens" + "\n" + \
                      "3                 DJ Koze" + "\n" + \
                      "4                 Solange"
    
    actual_output = repr(df1)

    assert actual_output == expected_output