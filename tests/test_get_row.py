from ie_pandas import DataFrame

import pytest

def get_row(self, index):
    if isinstance(index, int) == False:
        raise Exception(f"The index should be an integer.")
    elif (index > len(self.df[self.colindex[0]])) | index < 0:
        raise Exception(f"The index is out of range. It should be positive and smaller than {len(self.df[self.colindex[0]])}")
    else:
        return [self.df[i][index] for i in self.colindex]


dic = {'col_1': [3.0, 2.0, 1.0, 0.0],
       'col_2': ['as', 'bs', 'cs', 'ds'],
       'col_3': [3, 2, 1, 0],
       'col_4': [True, True, False, True]}

dict_pandas = DataFrame(dic)

test = [2.0, 'bs', 2, True]

expected_output = test

output = dict_pandas.get_row(1)

assert output == expected_output
