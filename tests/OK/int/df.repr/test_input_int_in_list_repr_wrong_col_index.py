from ie_pandas import DataFrame
import pytest

def test_input_int_in_list_repr_wrong_col_index():
    artists_age_list = [30, 53, 31, 47, 32]

    with pytest.raises(Exception) as exc_info:
        df = DataFrame(artists_age_list, colindex = ['AGE', 'TOOMANY'])

    exception_raised = exc_info.value

    assert exception_raised
