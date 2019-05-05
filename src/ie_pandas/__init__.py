import numpy as np


class DataFrame:
    # To create the DataFrame object
    def __init__(self, input_object, colindex="", rowindex="", axis=0):
        """
        input_object:
        Can be a list, a numpy array, a list of lists,
        a dictionary of lists, a dictionary of numpy arrays.
        Must contain integers, floats, booleans and/or strings.

        colindex:
        Should be a list of column names (strings).

        rowindex:
        Should be a list of row names (strings).

        axis:
        0 if input_object contains data by column (default).
        1 if input_object contains data by row.
        """

        # Check if input_object is empty or a single value
        try:
            len(input_object)
        except TypeError:
            raise Exception(
                f"The input should be a list (non-empty), a list of lists, "
                + f"a dictionary of lists, or a dictionary of numpy arrays. "
                + f"Now, it is a {type(input_object)}"
            )

        if len(input_object) == 0:
            raise Exception(
                f"The input should be a list (non-empty), a list of lists, "
                + f"a dictionary of lists, or a dictionary of numpy arrays. "
                + f"Now, it is a {type(input_object)}"
            )

        self.df = input_object

        #########################################################
        # PRE-CONVERT THE DF
        #########################################################

        # Special preparation for dictionaries
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
            elif type(list(dic.items())[0][1]) is np.ndarray:
                list_items = list(dic.items())
                col_names = []
                col_data = []
                for i in range(0, len(list_items)):
                    col_names.append(list_items[i][0])
                    col_data.append(list_items[i][1].tolist())
                return col_data, col_names

        # Prepare input_object by:
        # - converting it to a list,
        # - transposing it depending on axis parameter,
        # - collecting existing column names.
        def to_df(obj, axis):
            cols = ""
            rows = ""
            if type(obj) == np.ndarray:
                l_obj = obj.tolist()
                if axis == 0:
                    return l_obj, cols, rows
                else:
                    T_array = [[j] for j in l_obj]
                    return T_array, cols, rows
            elif type(obj) == dict:
                if axis == 0:
                    array_n_cols = dict_to_array(obj)
                    return array_n_cols[0], array_n_cols[1], rows
                else:
                    array_n_cols = dict_to_array(obj)
                    T_array = [
                        [row[i] for row in array_n_cols[0]]
                        for i in range(len(array_n_cols[0][0]))
                    ]
                    return T_array, cols, array_n_cols[1]
            elif type(obj) == list and type(obj[0]) == list:
                for lst in range(0, len(obj)):
                    if len(obj[lst]) == len(obj[lst + 1]):
                        if axis == 0:
                            return obj, cols, rows
                        else:
                            rang = range(len(obj[0]))
                            T_array = [[row[i] for row in obj] for i in rang]
                            return T_array, cols, rows
            else:
                if axis == 0:
                    return obj, cols, rows
                else:
                    T_array = [[j] for j in obj]
                    return T_array, cols, rows

        self.df, dict_cols, dict_rows = to_df(self.df, axis)

        #########################################################
        # CONFIGURATE THE DATAFRAME
        #########################################################

        # Check if the input_object if a list
        if type(self.df) == list:
            mylist = self.df
            typck = all(isinstance(j, (int, float, str, bool)) for j in mylist)
            if typck is True:
                mylist = [mylist]
            count_elements = len(mylist)
            count_records_first_element = len(mylist[0])

            # Check if elements of mylist are lists
            only_lists = True
            for i in range(0, count_elements):
                if type(mylist[i]) != list:
                    only_lists = False

            if only_lists is False:
                raise Exception(
                    f"The input should be a list (non-empty), "
                    + f"a list of lists, "
                    + f"a dictionary of lists, "
                    + f"or a dictionary of numpy arrays."
                )
            else:
                # Check if each element is int, float, bool or string
                for i in range(0, count_elements):
                    m = mylist[i]
                    t = all(isinstance(j, (int, float, bool, str)) for j in m)
                    if t is False:
                        raise Exception(
                            "Data types should be "
                            + "integer, float, boolean or string."
                        )

                # Check if each element contains consistent data types
                for i in range(0, count_elements):
                    ml = mylist[i]
                    typck = all(isinstance(j, type(mylist[i][0])) for j in ml)
                    if typck is False:
                        raise Exception(
                            "Data types should be consistent in each column."
                        )

                # Check each list has the same number of elements
                for i in range(0, count_elements):
                    if count_records_first_element != len(mylist[i]):
                        raise Exception(
                            "Your lists haven't the same number of elements!"
                        )

                # Apply the column index
                if (colindex == "") & (dict_cols == ""):
                    colindex = list(map(str, range(0, count_elements)))
                elif (colindex == "") & (dict_cols != ""):
                    colindex = dict_cols
                else:
                    if len(colindex) != count_elements:
                        raise Exception(
                            f"Not the right number of column names ! "
                            + f"It should be {count_elements}, "
                            + f"but it is {len(colindex)}."
                        )

                # Apply the row index
                if (rowindex == "") & (dict_rows == ""):
                    c = count_records_first_element
                    rowindex = list(map(str, range(0, c)))
                elif (rowindex == "") & (dict_rows != ""):
                    rowindex = dict_rows
                else:
                    if len(rowindex) != count_records_first_element:
                        raise Exception(
                            f"Not the right number of row names ! "
                            + f"It should be {count_records_first_element}, "
                            + f"but it is {len(rowindex)}."
                        )

                my_dict = dict(zip(colindex, mylist))
                self.colindex = list(colindex)
                self.rowindex = list(rowindex)
                self.df = my_dict
        else:
            raise Exception(
                f"The input should be a list (non-empty), a list of lists, "
                + f"a dictionary of lists, or a dictionary of numpy arrays. "
                + f"Now, it is a {type(self.df)}"
            )

    # To modify the content of the df
    def __setitem__(self, key, value):
        ck = all(isinstance(j, (int, float, bool, str)) for j in value)
        if key in self.colindex:
            if (
                (type(value) != list)
                | (len(value) != len(self.df[key]))
                | (ck is False)
                | (all(isinstance(j, type(value[0])) for j in value) is False)
            ):
                raise Exception(
                    f"The value to insert should be a list "
                    + f"of the same length as initial column, "
                    + f"with consistent data type among "
                    + f"integer, float, boolean or string."
                )
            else:
                self.df[key] = value
        elif isinstance(key, int) is False:
            raise Exception(f"Index should be an int or a column name.")
        elif (key < 0) | (key > len(self.df[self.colindex[0]])):
            raise Exception(
                f"The key is out of range. It should be "
                + f"positive integer and smaller "
                + f"than {len(self.df[self.colindex[0]])}"
            )
        elif (
            (type(value) != list)
            | (len(value) != len(self.df[self.colindex[key]]))
            | (ck is False)
            | (all(isinstance(j, type(value[0])) for j in value) is False)
        ):
            raise Exception(
                f"The value to insert should be a list "
                + f"of the same length as initial column, "
                + f"with consistent data type among "
                + f"integer, float, boolean or string."
            )
        else:
            self.df[self.colindex[key]] = value

    # To get the content of the df
    def __getitem__(self, key):
        if key in self.colindex:
            return np.array(self.df[key])
        elif isinstance(key, int) is False:
            raise Exception(f"Index should be an int or a column name.")
        elif (key < 0) | (key > len(self.df[self.colindex[0]])):
            raise Exception(
                f"The key is out of range. It should be "
                + f"positive integer and smaller "
                + f"than {len(self.df[self.colindex[0]])}"
            )
        else:
            return np.array(self.df[self.colindex[key]])

    # To get the content of one row
    def get_row(self, index):
        if index in self.rowindex:
            r = [self.df[i][self.rowindex.index(index)] for i in self.colindex]
            return r
        elif isinstance(index, int) is False:
            raise Exception(f"The index should be an integer or a row name.")
        elif (index > len(self.df[self.colindex[0]])) | (index < 0):
            raise Exception(
                f"The index is out of range. It should be "
                + f"positive and smaller than {len(self.df[self.colindex[0]])}"
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
                left_part = str(self.df[c][self.rowindex.index(r)])
                right_part = max_len_colindex[self.colindex.index(c)]
                nice_print += f"  {left_part:>{right_part}}"

        return nice_print

    # To find the sum of the elements of numerical columns
    def sum(self):
        copy = self
        sum_col = []
        cols = []
        for key in copy.colindex:
            # try:
            #     copy.df[key] = list(map(float, copy.df[key]))
            # except ValueError as ex:
            #     pass

            if all(isinstance(z, (int, float)) for z in copy.df[key]):
                cols.append(key)
                sum_col.append(sum(copy.df[key]))
        return sum_col

    # To find the minimum of the elements of numerical columns
    def min(self):
        copy = self
        min_col = []
        cols = []
        for key in copy.colindex:
            # try:
            #     copy.df[key] = list(map(float, copy.df[key]))
            # except ValueError as ex:
            #     pass

            if all(isinstance(z, (int, float)) for z in copy.df[key]):
                cols.append(key)
                min_col.append(min(copy.df[key]))
        return min_col

    # To find the maximum of the elements of numerical columns
    def max(self):
        copy = self
        max_col = []
        cols = []
        for key in copy.colindex:
            # try:
            #     copy.df[key] = list(map(float, copy.df[key]))
            # except ValueError as ex:
            #     pass

            if all(isinstance(z, (int, float)) for z in copy.df[key]):
                cols.append(key)
                max_col.append(max(copy.df[key]))
        return max_col

    # To find the median of the elements of numerical columns
    def median(self):
        copy = self
        median_col = []
        cols = []
        for key in copy.colindex:
            # try:
            #     copy.df[key] = list(map(float, copy.df[key]))
            # except ValueError as ex:
            #     pass

            if all(isinstance(z, (int, float)) for z in copy.df[key]):
                cols.append(key)
                median_col.append(np.median(copy.df[key]))
        return median_col

    # To find the mean of the elements of numerical columns
    def mean(self):
        copy = self
        mean_col = []
        cols = []
        for key in copy.colindex:
            # try:
            #     copy.df[key] = list(map(float, copy.df[key]))
            # except ValueError as ex:
            #     pass

            if all(isinstance(z, (int, float)) for z in copy.df[key]):
                cols.append(key)
                mean_col.append(np.mean(copy.df[key]))
        return mean_col

    # ADD YOUR OBJECTIVE HERE
    def head(self, n = 5):
        """
        This function returns the first five rows of the df, 
        or when specified differently, the first n rows.
        """
        copy = self
        head_df = []
        for key in copy.rowindex:
            while len(head_df) < n:
                head_df.append(copy.df[key])

        return head_df
    
    #def head(self, n=6):

        #n = min(n, len(self))
        #return self[0:n]

    #def tail(self, n=6):
     #   n = min(n, len(self))
      #  return self[(len(self)-n):len(self)]