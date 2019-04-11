import pytest

from ie_nlp_utils import tokenize 

def test_tokenize_returns_expected_list():
    sentence = "This is a sentence"

    expected_tokens = ["This", "is", "a", "sentence"]

    tokens = tokenize(sentence)

    assert tokens == expected_tokens


@pytest.mark.parametrize("sentence", [
    "THIS IS A SENTENCE",
    "THIS is a SENTENCE",
    "This iS a SenTenCe"
])
def test_tokenize_returns_expected_lowecase_list(sentence):
    sentence = "This is a sentence"

    expected_tokens = ["this", "is", "a", "sentence"]

    tokens = tokenize(sentence, lower=True)

    assert tokens == expected_tokens