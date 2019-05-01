from ie_pandas import DataFrame
import pytest

def test_list_colindex():
	dic = [3.0, 2.0, 1.0]
	df1 = DataFrame(dic)

	expected_output = ["0"]
	
	output = df1.colindex
	
	assert output == expected_output