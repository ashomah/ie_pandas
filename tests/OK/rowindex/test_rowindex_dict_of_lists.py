from ie_pandas import DataFrame
import pytest

def test_rowindex_dataframe_from_dict_of_lists():
	dic = {'col_1': [3.0, 2.0, 1.0], 'col_2': ['as', 'bs', 'cs'], 'col_3': [2, 1, 0], 'col_4': [True, True, False]}
	df1 = DataFrame(dic)

	expected_output = ['0', '1', '2']
	
	output = df1.rowindex
	
	assert output == expected_output