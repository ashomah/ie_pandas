from ie_pandas import DataFrame
import pytest

def string_input_in_dict_of_lists():
    artists_dict_of_lists = {'f_name':["Björk", "Chris", "Solange"], 'm_name':["James Blake", "DJ Koze", "David Byrne"]}
    dict_of_lists_df = DataFrame(artists_dict_of_lists)

    expected_output ="__       0             1/n0    Björk  James Blake/n1    Chris      DJ Koze/n2  Solange  David Byrne"
    actual_output = DataFrame(dict_of_lists_df)

    assert actual_output == expected_output