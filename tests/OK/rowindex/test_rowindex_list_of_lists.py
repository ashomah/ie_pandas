from ie_pandas import DataFrame
import pytest

def test_colindex_dataframe_from_list_of_lists():
	dic = [[3.0, 2.0, 1.0], ['as', 'bs', 'cs'], [2, 1, 0], [True, True, False]]
	df1 = DataFrame(dic, rowindex=["row_1", "row_2", "row_3"])

	expected_output = ['row_1', 'row_2', 'row_3']
	
	output = df1.rowindex
	
	assert output == expected_output