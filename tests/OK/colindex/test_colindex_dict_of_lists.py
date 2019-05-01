from ie_pandas import DataFrame
import pytest

def test_list_colindex():
	dic = {'0':[3.0, 2.0, 1.0], 'col_1':[3, 21, 63]}
	df1 = DataFrame(dic)

	expected_output = ["0", "col_1"]
	
	output = df1.colindex
	
	assert output == expected_output