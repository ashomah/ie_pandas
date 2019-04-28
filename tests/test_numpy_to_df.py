from ie_pandas import DataFrame

def test_to_df_end_type_dict():
    
    data = [
    ["col_1", "col_2", "col_3", "col_4"],
    [1,2,3,4],
    ["a", "b", "c", "d"],
    [5,6,7,8,],
    ["a", "b", "c", "d"]]

    data = np.array(data)

    expected_output = [['col_1', 'col_2', 'col_3', 'col_4'],[['3', '2', '1', '0'],['a', 'b', 'c', 'd'],['3', '2', '1', '0'],['a', 'b', 'c', 'd']]]

    output = DataFrame(data)

    assert output == expected_output, "DataType Wrong"
