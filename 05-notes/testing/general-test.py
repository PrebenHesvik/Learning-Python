import pytest

def test_is_in_pass():
    name = 'python'
    sentence = 'Python is the best programming language'
    with pytest.raises(AssertionError):
        assert name in sentence, 'name is missing, check spelling/case'
        
def test_is_in_pass():
    name = 'python'
    sentence = 'Python is the best programming language'
    assert name in sentence, 'name is missing, check spelling/case'