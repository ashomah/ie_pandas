from ie_pandas import DataFrame
import pytest


def test_input_mixed_in_list_head():
    obj = [30, 53.0, "31"]
    df = DataFrame(
        obj, rowindex=["AGE"], colindex=["A", "B", "C"], axis=1
    )

    expected_output = (
        "      A     B   C" + "\n" + "AGE  30  53.0  31"
    )

    actual_output = repr(df.head())

    assert actual_output == expected_output

