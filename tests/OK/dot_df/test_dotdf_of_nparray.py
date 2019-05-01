from ie_pandas import DataFrame
import numpy as np
import pytest

def test_list_rowindex():
	a = np.array([[3.0, 2.0, 1.0], [3, 21, 63]])
	df1 = DataFrame(a, colindex=["0", "row_1"])

	expected_output = {'0': [3.0, 2.0, 1.0], "row_1": [3, 21, 63]}
	
	output = df1.df
	
	assert output == expected_output