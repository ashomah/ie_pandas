from ie_pandas import DataFrame
import pytest

def test_axis_correctly_show_dict_of_lists():
	dic = {'name':['jb', 'cq'], 'album':[4, 2]}
	df1 = DataFrame(dic, axis=1)
	
	expected_output =" 	   0   1\nname  jb  cq\nalbum  4   2"
	output = repr(df1)
	
	assert output == expected_output