from ie_pandas import DataFrame
import pytest


def test_input_mixed_in_nparray_head():
    obj = np.array([30, 53.0, "31", True, 32])
    df = DataFrame(obj, colindex=["AGE"], rowindex=["A", "B", "C", "D", "E"])

    expected_output = (
        "    AGE"
        + "\n"
        + "A    30"
        + "\n"
        + "B  53.0"
    )

    actual_output = repr(df.head(2))

    assert actual_output == expected_output

