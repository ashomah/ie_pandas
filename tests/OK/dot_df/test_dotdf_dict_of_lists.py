from ie_pandas import DataFrame
import pytest

def test_structure_dataframe_from_dict_of_lists():
	dic = {'col_1': [3.0, 2.0, 1.0], 'col_2': ['as', 'bs', 'cs'], 'col_3': [2, 1, 0], 'col_4': [True, True, False]}
	df1 = DataFrame(dic)

	expected_output = {'col_1': [3.0, 2.0, 1.0], 'col_2': ['as', 'bs', 'cs'], 'col_3': [2, 1, 0], 'col_4': [True, True, False]}
	
	output = df1.df
	
	assert output == expected_output