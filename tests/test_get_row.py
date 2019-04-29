from ie_pandas import DataFrame

def get_row(self, index):
    if isinstance(index, int) == False:
        raise Exception(f"The index should be an integer.")
    elif (index > len(self.df[self.colindex[0]])) | index < 0:
        raise Exception(f"The index is out of range. It should be positive and smaller than {len(self.df[self.colindex[0]])}")
    else:
        return [self.df[i][index] for i in self.colindex]


artists_dict = {"artist_name": ["James Blake", "Björk", "Christine & The Queens", "DJ Koze", "Solange"], "age": [30, 53, 31, 47, 32], "albums": [4, 10, 2, 5, 4]}

df = DataFrame(artists_dict)


expected_output = ['Björk', '53', '10']

output = df.get_row(1)

assert output == expected_output