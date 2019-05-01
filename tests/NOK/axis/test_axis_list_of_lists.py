from ie_pandas import DataFrame
import pytest

def test_axis_correctly_show_list_of_lists():
	lol = [['as', 'bs', 'cs'], [2, 1, 0]]
	df1 = DataFrame(lol, colindex = ["1", "2"], axis=1)

	expected_output ="1    2     3\n0  'as'  'bs'  'cs'\n1     2     1     0"
	
	output = df1
	
	assert output == expected_output