from ie_pandas import DataFrame
import pytest


def test_input_mixed_in_dict_of_lists_repr_both_index_axis():
    obj = {
        "age": [30.1, 53.1, 31.1, 47.1, 32.1],
        "albums": [4, 10, 2, 5, 4],
        "C": ["a", "b", "c", "d", "e"],
        "D": [True, False, True, True, False],
    }

    with pytest.raises(Exception) as exc_info:
        df = DataFrame(
            obj,
            rowindex=["AGE", "ALBUMS", "C", "D"],
            colindex=["A", "B", "C", "D", "E"],
            axis=1,
        )

    exception_raised = exc_info.value

    assert exception_raised
