from ie_pandas import DataFrame

def test_to_df_end_type_dict():
    
    data = 1 #{'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd'], 'col_3': [3, 2, 1, 0], 'col_4': ['a', 'b', 'c', 'd']}

    expected_output = 1#[['col_1', 'col_2', 'col_3', 'col_4'],[['3', '2', '1', '0'],['a', 'b', 'c', 'd'],['3', '2', '1', '0'],['a', 'b', 'c', 'd']]]

    output = DataFrame(data)

    assert output == expected_output, "DataType Wrong"
