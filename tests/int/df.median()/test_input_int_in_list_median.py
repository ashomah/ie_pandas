from ie_pandas import DataFrame
import pytest


def test_input_int_in_list_median_odd():
    obj = [30, 53, 31, 47, 32]
    df = DataFrame(obj, colindex=["AGE"], rowindex=["A", "B", "C", "D", "E"])

    expected_output = [32.0]

    actual_output = df.median()

    assert actual_output == expected_output


def test_input_int_in_list_median_even():
    obj = [30, 53, 31, 47, 32, 100]
    df = DataFrame(obj, colindex=["AGE"], rowindex=["A", "B", "C", "D", "E", "F"])

    expected_output = [39.5]

    actual_output = df.median()

    assert actual_output == expected_output
