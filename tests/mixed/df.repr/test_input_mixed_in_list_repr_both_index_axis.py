from ie_pandas import DataFrame
import pytest

def test_input_mixed_in_list_repr_both_index_axis():
    obj = [30, 53.0, '31', True, 32]
    df = DataFrame(obj, rowindex = ['AGE'], colindex = ['A', 'B', 'C', 'D', 'E'], axis=1)

    expected_output = "      A     B   C     D   E" + "\n" + \
                      "AGE  30  53.0  31  True  32"

    actual_output = repr(df)

    assert actual_output == expected_output