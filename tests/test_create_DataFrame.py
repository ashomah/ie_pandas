
from ie_pandas import DataFrame

def test_create_dataframe():
	dic = {'col_1': [3.0, 2.0, 1.0], 'col_2': ['as', 'bs', 'cs'], 'col_3': [2, 1, 0], 'col_4': [True, True, False]}
	
	expected_output = "__col_1  col_2  col_3  col_4/n0   3.0   'as'      2   True/n1   2.0   'bs'      1   True/n2   1.0   'cs'      0  False"
	
	output = DataFrame(dic)
	
	assert output == expected_output