from ie_pandas import DataFrame

import pytest

import numpy as np


def __getitem__(self, key):
        if key in self.colindex:
            return np.array(self.df[key])
        elif (isinstance(key, int) == False) | (key < 0) | (key > len(self.df[self.colindex[0]])):
                raise Exception(f"The key is out of range. It should be positive integer and smaller than {len(self.df[self.colindex[0]])}")
        else:
            return np.array(self.df[self.colindex[key]])


dic = {'col_1': [3.0, 2.0, 1.0, 0.0],
       'col_2': ['as', 'bs', 'cs', 'ds'],
       'col_3': [3, 2, 1, 0],
       'col_4': [True, True, False, True]}

dict_pandas = DataFrame(dic)

testing = [True, True, False, True]

expected_output = np.array(testing)

output = dict_pandas['col_4']

assert output == expected_output


