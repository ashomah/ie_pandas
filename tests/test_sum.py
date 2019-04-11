from ie_nlp_utils import sum_numbers

def testSumTwoNumbersGivesExpectedResult():
    a = 2
    b = 2

    expected_output = 4

    output = sum_numbers(a, b)

    assert output == expected_output, "Math is wrong"
