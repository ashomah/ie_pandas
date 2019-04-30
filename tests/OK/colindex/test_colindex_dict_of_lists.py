from ie_pandas import DataFrame
import pytest

def test_colindex_dataframe_from_dict_of_lists():
	dic = {'col_1': [3.0, 2.0, 1.0], 'col_2': ['as', 'bs', 'cs'], 'col_3': [2, 1, 0], 'col_4': [True, True, False]}
	df1 = DataFrame(dic)

	expected_output = ['col_1', 'col_2', 'col_3', 'col_4']
	
	output = df1.colindex
	
	assert output == expected_output