import pytest
from chatbot import valid_search , morning , afternoon 

def test_valid_search():
    assert valid_search("martin Garrix") == True
    assert valid_search("rick roll") == True

    
def test_morning():
    assert morning(10) == True
    assert morning(13) == False
    
def test_afternoon():
    assert afternoon(14) == True
    assert afternoon(22) == False