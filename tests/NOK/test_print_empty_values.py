from ie_pandas import DataFrame
import pytest

def test_print_dataframe_from_empty_value():

	expected_output = "-----------------------------TypeErrorTraceback (most recent call last)<ipython-input-4-812a8017b3b3> in <module>----> 1 df = DataFrame()\n\nTypeError: _init_() missing 1 required positional argument: 'input_object'"
	
	output = DataFrame("")
	assert output == expected_output

	output = DataFrame()
	assert output == expected_output

	output = DataFrame(['',''])
	assert output == expected_output