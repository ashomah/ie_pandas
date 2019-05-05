from ie_pandas import DataFrame
import pytest


def test_input_mixed_in_dict_of_nparray_shorter_n_head():
obj = {
        "age": np.array([30.1, 53.1]),
        "albums": np.array([4, 10]),
        "C": np.array(["a", "b"]),
        "D": np.array([True, False]),
    }
    df = DataFrame(
        obj,
        colindex=["AGE", "ALBUMS", "C", "D"],
        rowindex=["A", "B"],
    )

    expected_output = (
        "    AGE  ALBUMS  C      D"
        + "\n"
        + "A  30.1       4  a   True"
        + "\n"
        + "B  53.1      10  b  False"
    )

    actual_output = repr(df.head())

    assert actual_output == expected_output

