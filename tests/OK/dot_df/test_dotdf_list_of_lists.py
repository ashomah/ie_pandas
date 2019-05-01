from ie_pandas import DataFrame
import pytest

def test_structure_dataframe_from_list_of_lists():
	dic = [[3.0, 2.0, 1.0], ['as', 'bs', 'cs'], [2, 1, 0], [True, True, False]]
	df1 = DataFrame(dic, colindex=['col_1','col_2','col_3','col_4'])

	expected_output = {'col_1': [3.0, 2.0, 1.0], 'col_2': ['as', 'bs', 'cs'], 'col_3': [2, 1, 0], 'col_4': [True, True, False]}
	
	output = df1.df
	
	assert output == expected_output