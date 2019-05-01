import numpy as np


class DataFrame:
    def __init__(self, input_object, colindex="", rowindex="", axis=0):
        """
        input_object: can be a list, a list of lists, a dictionary, a numpy array.
        colindex: should be a list of column names.
        rowindex: should be a list of row names.
        axis: 0 if input_object contains data by column (default). 1 if input_object contains data by row.
        """

        # Check if input_object is empty or a single value
        try:
            len(input_object)
        except:
            raise Exception(
                f"The input should be a list (non-empty), a list of lists, a dictionary of lists, or a dictionary of numpy arrays. Now, it is a {type(input_object)}"
            )

        if len(input_object) == 0:
            raise Exception(
                f"The input should be a list (non-empty), a list of lists, a dictionary of lists, or a dictionary of numpy arrays. Now, it is a {type(input_object)}"
            )

        self.df = input_object

        #########################################################
        # PRE-CONVERT THE DF
        #########################################################

        def dict_to_array(dic):
            """
            Function to convert dictionaries to numpy arrays
            """
            # From dictionary of lists
            if type(list(dic.items())[0][1]) == list:
                list_items = list(dic.items())
                col_names = []
                col_data = []
                for i in range(0, len(list_items)):
                    col_names.append(list_items[i][0])
                    col_data.append(list_items[i][1])
                return col_data, col_names

            # From dictionary of numpy arrays
            elif str(type(list(dic.items())[0][1])) == "<class 'numpy.ndarray'>":
                list_items = list(dic.items())
                col_names = []
                col_data = []
                for i in range(0, len(list_items)):
                    col_names.append(list_items[i][0])
                    col_data.append(list_items[i][1].tolist())
                return col_data, col_names

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
                    return array_n_cols[0], array_n_cols[1]
                else:
                    array_n_cols = dict_to_array(obj)
                    T_array = [
                        [row[i] for row in array_n_cols[0]]
                        for i in range(len(array_n_cols[0][0]))
                    ]
                    return T_array, array_n_cols[1]
            elif type(obj) == list and type(obj[0]) == list:
                for lst in range(0, len(obj)):
                    if len(obj[lst]) == len(obj[lst + 1]):
                        if axis == 0:
                            return np.array(obj).tolist(), cols
                        else:
                            return np.array(obj).T.tolist(), cols
            else:
                if axis == 0:
                    return obj, cols
                else:
                    T_array = [[j] for j in obj]
                    return T_array, cols

        self.df, dict_cols = to_df(self.df, axis)

        #########################################################
        # CONFIGURATE THE DATAFRAME
        #########################################################

        # Check if the input_object if a list
        if type(self.df) == list:
            mylist = self.df
            if all(isinstance(j, (int, float, str, bool)) for j in mylist) == True:
                mylist = [mylist]
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
                    if (
                        all(isinstance(j, (int, float, bool, str)) for j in mylist[i])
                        == False
                    ):
                        raise Exception(
                            "Data types should be integer, float, boolean or string."
                        )

                # Check if each element contains consistent data types
                for i in range(0, count_elements):
                    if (
                        all(isinstance(j, type(mylist[i][0])) for j in mylist[i])
                        == False
                    ):
                        raise Exception(
                            "Data types should be consistent within each column."
                        )

                # Check each list has the same number of elements
                for i in range(0, count_elements):
                    if count_records_first_element != len(mylist[i]):
                        raise Exception(
                            "Your lists don't have the same number of elements!"
                        )

                # Apply the column index
                if (colindex == "") & (dict_cols == ""):
                    colindex = list(map(str, range(0, count_elements)))
                elif (colindex == "") & (dict_cols != ""):
                    colindex = dict_cols
                else:
                    if len(colindex) != count_elements:
                        raise Exception(
                            f"Not the right number of column names ! It should be {count_elements}, but it is {len(colindex)}."
                        )

                # Apply the row index
                if rowindex == "":
                    rowindex = list(map(str, range(0, count_records_first_element)))
                else:
                    if len(rowindex) != count_records_first_element:
                        raise Exception(
                            f"Not the right number of row names ! It should be {count_records_first_element}, but it is {len(rowindex)}."
                        )

                my_dict = dict(zip(colindex, mylist))
                self.colindex = list(colindex)
                self.rowindex = list(rowindex)
                self.df = my_dict
        else:
            raise Exception(
                f"The input should be a list (non-empty), a list of lists, a dictionary of lists, or a dictionary of numpy arrays. Now, it is a {type(self.df)}"
            )

    # To modify the content of the df
    def __setitem__(self, key, value):
        if key in self.colindex:
            self.df[key] = value
        elif (
            (isinstance(key, int) == False)
            | (key < 0)
            | (key > len(self.df[self.colindex[0]]))
        ):
            raise Exception(
                f"The key is out of range. It should be positive integer and smaller than {len(self.df[self.colindex[0]])}"
            )
        else:
            self.df[self.colindex[key]] = value

    # To get the content of the df
    def __getitem__(self, key):
        if key in self.colindex:
            return np.array(self.df[key])
        elif (
            (isinstance(key, int) == False)
            | (key < 0)
            | (key > len(self.df[self.colindex[0]]))
        ):
            raise Exception(
                f"The key is out of range. It should be positive integer and smaller than {len(self.df[self.colindex[0]])}"
            )
        else:
            return np.array(self.df[self.colindex[key]])

    # To get the content of one row
    def get_row(self, index):
        if isinstance(index, int) == False:
            raise Exception(f"The index should be an integer.")
        elif (index > len(self.df[self.colindex[0]])) | index < 0:
            raise Exception(
                f"The index is out of range. It should be positive and smaller than {len(self.df[self.colindex[0]])}"
            )
        else:
            return [self.df[i][index] for i in self.colindex]

    # To print the df
    def __repr__(self):
        first = 1
        max_len_rowindex = len(max(self.rowindex, key=len))
        max_len_colindex = []
        df_data = np.array(list(self.df.values()))
        nice_print = f"{'':<{max_len_rowindex}}"
        for c in self.colindex:
            max_col = len(max(list(map(str, self.df[c])), key=len))
            if max_col > len(c):
                max_len_colindex.append(max_col)
            else:
                max_len_colindex.append(len(c))
            nice_print += f"  {c:>{max_len_colindex[self.colindex.index(c)]}}"
        for r in self.rowindex:
            nice_print += f"\n{r:<{max_len_rowindex}}"
            for c in self.colindex:
                nice_print += f"  {str(self.df[c][self.rowindex.index(r)]):>{max_len_colindex[self.colindex.index(c)]}}"

        return nice_print

    def sum(self):
        copy = self
        sum_col = []
        cols = []
        for key in copy.colindex:
            try:
                copy.df[key] = list(map(float, copy.df[key]))
            except ValueError as ex:
                pass

            if all(isinstance(z, (int, float)) for z in copy.df[key]):
                cols.append(key)
                sum_col.append(sum(copy.df[key]))
        return sum_col

    def min(self):
        copy = self
        min_col = []
        cols = []
        for key in copy.colindex:
            try:
                copy.df[key] = list(map(float, copy.df[key]))
            except ValueError as ex:
                pass

            if all(isinstance(z, (int, float)) for z in copy.df[key]):
                cols.append(key)
                min_col.append(min(copy.df[key]))
        return min_col

    def max(self):
        copy = self
        max_col = []
        cols = []
        for key in copy.colindex:
            try:
                copy.df[key] = list(map(float, copy.df[key]))
            except ValueError as ex:
                pass

            if all(isinstance(z, (int, float)) for z in copy.df[key]):
                cols.append(key)
                max_col.append(max(copy.df[key]))
        return max_col

    def median(self):

        copy = self
        median_col = []
        cols = []
        for key in copy.colindex:
            try:
                copy.df[key] = list(map(float, copy.df[key]))
            except ValueError as ex:
                pass

            if all(isinstance(z, (int, float)) for z in copy.df[key]):
                cols.append(key)
                median_col.append(np.median(copy.df[key]))
        return median_col

    def mean(self):

        copy = self
        mean_col = []
        cols = []
        for key in copy.colindex:
            try:
                copy.df[key] = list(map(float, copy.df[key]))
            except ValueError as ex:
                pass

            if all(isinstance(z, (int, float)) for z in copy.df[key]):
                cols.append(key)
                mean_col.append(np.mean(copy.df[key]))
        return mean_col

# To indicate the script has been run when importing the package
print("Done __init__.py")
