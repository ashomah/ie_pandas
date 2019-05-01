from ie_pandas import DataFrame
import pytest

def test_axis_correctly_show_dict_of_lists():
    artists_dict_of_lists = {'age':['as', 'az'], 'albums':['bs', 'bz']}
	df1 = DataFrame(artists_dict_of_lists, colindex = ["1", "2"], axis=1)

	expected_output ="     1     2\n0  'as'  'az'\n1  'bs'  'bz'"
	
	output = df1
	
	assert output == expected_output