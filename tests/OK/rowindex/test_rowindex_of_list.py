from ie_pandas import DataFrame
import pytest

def test_list_rowindex():
	dic = [3.0, 2.0, 1.0]
	df1 = DataFrame(dic)

	expected_output = ["0", "1", "2"]
	
	output = df1.rowindex
	
	assert output == expected_output