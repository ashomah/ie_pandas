from ie_pandas import DataFrame
import numpy as np
import pytest

def test_list_np_arrays():
	a = np.array([[3.0, 2.0, 1.0], [3, 21, 63]])
	df1 = DataFrame(a, colindex=["0", "col_1"])

	expected_output = ["0", "col_1"]
	
	output = df1.colindex
	
	assert output == expected_output