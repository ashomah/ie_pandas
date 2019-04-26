class DataFrame:

    import numpy as np

    def __init__(self, input_object, colindex = '', rowindex = ''):
        self.df = input_object
        # self.name = hex(id(self))
        # self.input_object = to_array(self.input_object)

        # Check if the input_object if a list
        if type(input_object) == list:
            mylist = input_object
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
                # Check each list has the same number of elements
                for i in range(0, count_elements):
                    if count_records_first_element != len(mylist[i]):
                        raise Exception("Your lists don't have the same number of elements!")

                # Apply the column index
                if colindex == '':
                    colindex = range(0, count_elements)
                else:
                    if len(colindex) != count_elements:
                        raise Exception(f"Not the right number of column names ! It shoul be {count_elements}, but it is {len(colindex)}.")

                # Apply the row index
                if rowindex == '':
                    rowindex = range(0, count_records_first_element)
                else:
                    if len(rowindex) != count_records_first_element:
                        raise Exception(f"Not the right number of column names ! It shoul be {count_records_first_element}, but it is {len(rowindex)}.")

                my_dict = dict(zip(colindex, mylist))
                my_dict['colindex'] = list(colindex)
                my_dict['rowindex'] = list(rowindex)
                self.df = my_dict
        else:
            raise Exception(f"The input should be a list. Now, it is a {type(self.df)}")


    # To modify the content of the df
    def __setitem__(self, key, value):
        self.df[key] = value

    # To get the content of the df
    def __getitem__(self, key):
        return self.df[key]

    # To print the df
    def __repr__(self):
        list_col = self.df['colindex']
        n_print = { key:value for key,value in self.df.items() if key in list_col}
        return f"{n_print}" + \
            "\n\n" + \
            f"It is a {type(self.df).__name__}." + \
            "\n\n" + \
            f"Full content:" + "\n" + \
            f"{self.df}."
    
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
     

# def dict_to_array(dic):
#     """
#     Function to convert dictionaries to numpy arrays
#     """

#     # From dictionary of lists
#     if type(list(dic.items())[0][1]) == list:
#         arr_dic = np.array(list(dic.items()))
#         ls = []
#         for i in arr_dic:
#             for j in i:
#                 if type(j) != list:
#                     ls.append(j)
#                 elif type(j) == list:
#                     for k in j:
#                         ls.append(k)
#         ls2 = []
#         for item in range(int((len(ls) / len(arr_dic)))):
#             counter = 0
#             for ii in range(int(len(arr_dic))):
#                 ls2.append(ls[item + counter])
#                 counter += int((arr_dic.itemsize / 2) + 1)
#         return np.reshape(
#             np.array(ls2), ((int(arr_dic.itemsize / 2) + 1, len(arr_dic)))
#         )

#     # From dictionary of numpy arrays
#     elif str(type(list(dic.items())[0][1])) == "<class 'numpy.ndarray'>":
#         arr_dic = np.array(list(my_dict.items()))
#         ls = []
#         for i in arr_dic:
#             for j in i:
#                 if str(type(j)) != "<class 'numpy.ndarray'>":
#                     ls.append(j)
#                 elif str(type(j)) == "<class 'numpy.ndarray'>":
#                     for k in j:
#                         ls.append(k)
#         ls2 = []
#         for item in range(int((len(ls) / len(arr_dic)))):
#             counter = 0
#             for ii in range(int(len(arr_dic))):
#                 ls2.append(ls[item + counter])
#                 counter += int((arr_dic.itemsize / 2))
#         return np.reshape(
#             np.array(ls2), ((int(arr_dic.itemsize / 2), len(arr_dic)))
#         )

# To indicate the script has been run when importing the package
print("Done __init__.py")
