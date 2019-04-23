class DataFrame:

    def __init__(self, input_object):
        self.input_object = input_object

    def __repr__(self):
        return f"ie_pandas object called '{self.input_object}'."

    def hello(self):
        print('Hello')

class TEST_DF:
    def __init__(self, input_obj):
        self.input_obj = input_obj

    def __repr__(self):
        return f"ie_pandas object called '{self.input_obj}'."

print('I am %s' % __name__)