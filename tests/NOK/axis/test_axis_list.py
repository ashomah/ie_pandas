from ie_pandas import DataFrame
import pytest

def test_axis_correctly_show_list():
	list = [True, True, False]
	df1 = DataFrame(list, colindex = ["1", "2", "3"], axis=1)

	expected_output ="    1     2      3\n0  True  True  False"
	
	output = df1
	
	assert output == expected_output