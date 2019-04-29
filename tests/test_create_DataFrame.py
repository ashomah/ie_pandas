
from ie_pandas import DataFrame

def test_create_dataframe():

	dic = {'col_1': [3.0, 2.0, 1.0, 0.0],
       	'col_2': ['as', 'bs', 'cs', 'ds'],
       	'col_3': [3, 2, 1, 0],
       	'col_4': [True, True, False, True]}


df=DataFrame(dic)