class DataFrame:

    def __init__(self, input_object, colindex = '', rowindex = '', axis = 0):
        '''
        input_object: can be a list, a list of lists, a dictionary, a numpy array.
        colindex: should be a list of column names.
        rowindex: should be a list of row names.
        axis: 0 if input_object contains data by column (default). 1 if input_object contains data by row.
        '''
        import numpy as np
        self.df = input_object
        # self.name = hex(id(self))
        # self.input_object = to_array(self.input_object)

        #########################################################
        # PRE-CONVERT THE DF
        #########################################################

        def dict_to_array(dic):
            """
            Function to convert dictionaries to numpy arrays
            """

            # From dictionary of lists
            if type(list(dic.items())[0][1]) == list:
                arr_dic = np.array(list(dic.items()))
                cols = []
                ls = []
                for i in arr_dic:
                    for j in i:
                        if type(j) != list:
                            cols.append(j)
                        elif type(j) == list:
                            for k in j:
                                ls.append(k)
                ls2 = []
                for item in range(int((len(ls) / len(arr_dic)))):
                    counter = 0
                    for ii in range(int(len(arr_dic))):
                        ls2.append(ls[item + counter])
                        counter += int((arr_dic.itemsize / 2))
                return np.reshape(
                    np.array(ls2), ((int(arr_dic.itemsize / 2), len(arr_dic)))
                ), cols

            # From dictionary of numpy arrays
            elif str(type(list(dic.items())[0][1])) == "<class 'numpy.ndarray'>":
                arr_dic = np.array(list(my_dict.items()))
                cols = []
                ls = []
                for i in arr_dic:
                    for j in i:
                        if str(type(j)) != "<class 'numpy.ndarray'>":
                            cols.append(j)
                        elif str(type(j)) == "<class 'numpy.ndarray'>":
                            for k in j:
                                ls.append(k)
                ls2 = []
                for item in range(int((len(ls) / len(arr_dic)))):
                    counter = 0
                    for ii in range(int(len(arr_dic))):
                        ls2.append(ls[item + counter])
                        counter += int((arr_dic.itemsize / 2))
                return cols, np.reshape(
                    np.array(ls2), ((int(arr_dic.itemsize / 2), len(arr_dic)))
                ), cols

        def to_df(obj, axis):
            cols = ""
            if str(type(obj)) == "<class 'numpy.ndarray'>":
                if axis == 0:
                    return obj.tolist(), cols
                else:
                    return obj.T.tolist(), cols
            elif type(obj) == list and obj[0] == [int or str or float]:
                if axis == 0:
                    return np.array(obj).tolist(), cols
                else:
                    return np.array(obj).T.tolist(), cols
            elif type(obj) == dict:
                if axis == 0:
                    array_n_cols = dict_to_array(obj)
                    return array_n_cols[0].T.tolist(), array_n_cols[1]
                else:
                    array_n_cols = dict_to_array(obj)
                    return array_n_cols[0].tolist(), array_n_cols[1]
            elif type(obj) == list and obj[0] == list:
                for lst in range(obj-1):
                    if len(obj[lst]) == len(obj[lst+1]):
                        if axis == 0:
                            return np.array(obj).tolist(), cols
                        else:
                            return np.array(obj).T.tolist(), cols
            else:
                if axis == 0:
                    return obj, cols
                else:
                    return np.array(obj).T.tolist(), cols

        self.df, dict_cols = to_df(self.df, axis)

        #########################################################
        # CONFIGURATE THE DATAFRAME
        #########################################################

        # Check if the input_object if a list
        if type(self.df) == list:
            mylist = self.df
            count_elements = len(mylist)
            count_records_first_element = len(mylist[0])

            # Check if elements of mylist are lists
            only_lists = True
            for i in range(0, count_elements):
                if type(mylist[i]) != list:
                    only_lists = False
            
            if only_lists == False:
                raise Exception("Only list of lists is accepted for now...")
            else:
                # Check if each element is int, float, bool or string
                for i in range(0, count_elements):
                    if all(isinstance(j, (int, float, bool, str)) for j in mylist[i]) == False:
                        print(type(mylist[i]))
                        raise Exception("Data types should be integer, float, boolean or string.")
                        
                # Check if each element contains consistent data types
                for i in range(0, count_elements):
                    if all(isinstance(j, type(mylist[i][0])) for j in mylist[i]) == False:
                        raise Exception("Data types should be consistent within each column.")
                        
                # Check each list has the same number of elements
                for i in range(0, count_elements):
                    if count_records_first_element != len(mylist[i]):
                        raise Exception("Your lists don't have the same number of elements!")

                # Apply the column index
                if (colindex == '') & (dict_cols == ''):
                    colindex = range(0, count_elements)
                elif (colindex == '') & (dict_cols != ''):
                    colindex = dict_cols
                else:
                    if len(colindex) != count_elements:
                        raise Exception(f"Not the right number of column names ! It shoul be {count_elements}, but it is {len(colindex)}.")

                # Apply the row index
                if rowindex == '':
                    rowindex = range(0, count_records_first_element)
                else:
                    if len(rowindex) != count_records_first_element:
                        raise Exception(f"Not the right number of row names ! It shoul be {count_records_first_element}, but it is {len(rowindex)}.")

                my_dict = dict(zip(colindex, mylist))
                self.colindex = list(colindex)
                self.rowindex = list(rowindex)
                self.df = my_dict
        else:
            raise Exception(f"The input should be a list, a list of lists, a dictionary, or a numpy array. Now, it is a {type(self.df)}")

    # To modify the content of the df
    def __setitem__(self, key, value):
        self.df[key] = value    # SHOULD BE MODIFIED TO CHECK IF THE KEY IS IN COLINDEX

    # To get the content of the df
    def __getitem__(self, key):
        import numpy as np
        if key in self.colindex:
            return np.array(self.df[key])
        elif (isinstance(key, int) == False) | (key < 0) | (key > len(self.df[self.colindex[0]])):
                raise Exception(f"The key is out of range. It should be positive integer and smaller than {len(self.df[self.colindex[0]])}")
        else:
            return np.array(self.df[self.colindex[key]])

    # To get the content of one row
    def get_row(self, index):
        if isinstance(index, int) == False:
            raise Exception(f"The index should be an integer.")
        elif (index > len(self.df[self.colindex[0]])) | index < 0:
            raise Exception(f"The index is out of range. It should be positive and smaller than {len(self.df[self.colindex[0]])}")
        else:
            return [self.df[i][index] for i in self.colindex]

    # To print the df
    def __repr__(self):
        import numpy as np
        n_print = ""
        first = 1
        for key in self.colindex:
            for i in range(len(list(self.df.items()))):
                if key == list(self.df.items())[i][0]:
                    if first == 1:
                        first = 0
                        n_print = f"{list(self.df.items())[i][0]} : {list(self.df.items())[i][1]}" 
                    else:
                        n_print += f"\n{list(self.df.items())[i][0]} : {list(self.df.items())[i][1]}"                 
        return f"{n_print}"

    # def __repr__(self):
    #     import numpy as np
    #     n_print = { key:value for key,value in self.df.items() if key in self.colindex}
    #     return f"{n_print}"

    # @staticmethod
    # def nice_print ():
    #     list_col = self.df['colindex']
    #     n_print = { key:value for key,value in self.df.items() if key in list_col}
    #     return f"{n_print}"

    # def pretty(self, list_col):
    #     n_print = {key:value for key,value in self.df.items() if key in list_col}
    #     return n_print

# def to_array(obj):
#     """
#     Function to convert any object to numpy array
#     """

#     if str(type(obj)) == "<class 'numpy.ndarray'>":
#         return obj
#     elif type(obj) == list and obj[0] == [int or str or float]:
#         return np.array(obj)
#     elif type(obj) == dict:
#         return dict_to_array(obj)
#     elif type(obj) == list and obj[0] == list:
#         for lst in range(obj - 1):
#             if len(obj[lst]) == len(obj[lst + 1]):
#                 return np.array(obj)
     
# To indicate the script has been run when importing the package
print("Done __init__.py")
