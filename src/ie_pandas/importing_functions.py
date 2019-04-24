# Working function -> dictionaries to np arrays
def dict_to_array(dic):

    # From dictionary of lists

    if type(list(dic.items())[0][1]) == list:
        arr_dic = np.array(list(dic.items()))
        ls = []
        for i in arr_dic:
            for j in i:
                if type(j) != list:
                    ls.append(j)
                elif type(j) == list:
                    for k in j:
                        ls.append(k)
        ls2 = []
        for item in range(int((len(ls) / len(arr_dic)))):
            counter = 0
            for ii in range(int(len(arr_dic))):
                ls2.append(ls[item + counter])
                counter += int((arr_dic.itemsize / 2) + 1)
        return np.reshape(
            np.array(ls2), ((int(arr_dic.itemsize / 2) + 1, len(arr_dic)))
        )

    # From dictionary of numpy arrays

    elif str(type(list(dic.items())[0][1])) == "<class 'numpy.ndarray'>":
        arr_dic = np.array(list(my_dict.items()))
        ls = []
        for i in arr_dic:
            for j in i:
                if str(type(j)) != "<class 'numpy.ndarray'>":
                    ls.append(j)
                elif str(type(j)) == "<class 'numpy.ndarray'>":
                    for k in j:
                        ls.append(k)
        ls2 = []
        for item in range(int((len(ls) / len(arr_dic)))):
            counter = 0
            for ii in range(int(len(arr_dic))):
                ls2.append(ls[item + counter])
                counter += int((arr_dic.itemsize / 2))
        return np.reshape(np.array(ls2), ((int(arr_dic.itemsize / 2), len(arr_dic))))


# import function to convert anything into np arrays


def to_array(obj):
    if str(type(obj)) == "<class 'numpy.ndarray'>":
        return obj
    elif type(obj) == list and obj[0] == [int or str or float]:
        return np.array(obj)
    elif type(obj) == dict:
        return dict_to_array(obj)
    elif type(obj) == list and obj[0] == list:
        for lst in range(obj - 1):
            if len(obj[lst]) == len(obj[lst + 1]):
                return np.array(obj)