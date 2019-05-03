from ie_pandas import DataFrame
import pytest


def test_input_int_in_df_both_index_axis():
    obj = {"age": [30, 53, 31, 47, 32], "albums": [4, 10, 2, 5, 4]}
    df = DataFrame(
        obj, rowindex=["AGE", "ALBUMS"], colindex=["A", "B", "C", "D", "E"], axis=1
    )

    expected_output = {
        "A": [30, 4],
        "B": [53, 10],
        "C": [31, 2],
        "D": [47, 5],
        "E": [32, 4],
    }

    actual_output = df.df

    assert actual_output == expected_output
