from ie_pandas import DataFrame
import pytest

def test_colindex_dataframe_from_list_of_lists():
	dic = [[3.0, 2.0, 1.0], ['as', 'bs', 'cs'], [2, 1, 0], [True, True, False]]
	df1 = DataFrame(dic)

	expected_output = ['col_1', 'col_2', 'col_3', 'col_4']
	
	output = df1.colindex
	
	assert output == expected_output