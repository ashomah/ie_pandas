from ie_pandas import DataFrame
import pytest

def test_axis_correctly_show_list():
    a = np.array([[3.0, 2.0, 1.0], [3, 21, 63]])
	df1 = DataFrame(a, colindex = ["1", "2", "3"], axis=1)

	expected_output ="    1    2    3\n0  3.0  2.0  1.0"
	
	output = df1
	
	assert output == expected_output