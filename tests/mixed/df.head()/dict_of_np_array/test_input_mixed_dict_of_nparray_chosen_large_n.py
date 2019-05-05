from ie_pandas import DataFrame
import pytest


def test_input_mixed_in_dict_of_nparray_large_n_head():
    obj = {
        "age": np.array([30.1, 53.1, 31.1, 47.1, 32.1]),
        "albums": np.array([4, 10, 2, 5, 4]),
        "C": np.array(["a", "b", "c", "d", "e"]),
        "D": np.array([True, False, True, True, False]),
    }
    df = DataFrame(
        obj,
        colindex=["AGE", "ALBUMS", "C", "D"],
        rowindex=["A", "B", "C", "D", "E"],
    )

    expected_output = (
        "    AGE  ALBUMS  C      D"
        + "\n"
        + "A  30.1       4  a   True"
        + "\n"
        + "B  53.1      10  b  False"
        + "\n"
        + "C  31.1       2  c   True"
        + "\n"
        + "D  47.1       5  d   True"
        + "\n"
        + "E  32.1       4  e  False"
    )

    actual_output = repr(df.head(20))

    assert actual_output == expected_output

