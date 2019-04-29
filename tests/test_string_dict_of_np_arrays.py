from ie_pandas import DataFrame
import pytest

def string_input_in_dict_of_lists():
    artists_dict_of_lists = [["Björk", "Chris", "Solange"], ["James Blake", "DJ Koze", "David Byrne"]]
    np_array = np.array(artists_dict_of_lists)
    dict_of_lists_df = DataFrame(np_array, rowindex=['A', 'B', 'C'])

    expected_output ="__       0             1/nA    Björk  James Blake/nB    Chris      DJ Koze/nC  Solange  David Byrne"

    actual_output = DataFrame(dict_of_lists_df)

    assert actual_output == expected_output