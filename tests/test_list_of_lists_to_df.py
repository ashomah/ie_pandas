from ie_pandas import DataFrame

def test_to_df_end_type_dict():
    
    data = {data = [
    ["col_1", "col_2", "col_3", "col_4"],
    [1,2,3,4],
    ["a", "b", "c", "d"],
    [5,6,7,8,],
    ["a", "b", "c", "d"],
]

    expected_output = [['col_1', 'col_2', 'col_3', 'col_4'],
    [['1', 'a', '5', 'a'],
    ['2', 'b', '6', 'b'],
    ['3', 'c', '7', 'c'],
    ['4', 'd', '8', 'd']]]
    output = DataFrame(data)

    assert output == expected_output, "DataType Wrong"
