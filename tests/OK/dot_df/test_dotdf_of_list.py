from ie_pandas import DataFrame
import pytest

def test_structure_dataframe_from_list():
	dic = ['as', 'bs', 'cs']
	df1 = DataFrame(dic, colindex=['only_col'])

	expected_output = {'only_col': ['as', 'bs', 'cs']}
	
	output = df1.df
	
	assert output == expected_output