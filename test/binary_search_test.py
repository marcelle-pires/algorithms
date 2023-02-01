from src.binary_search import binary_search 

def test_binary_search_sucessfully():
    list = [1, 2, 3, 7, 8]
    value = 2
    assert binary_search(list, value) == 1 

def test_binary_search_sucessfully_with_char_values():
    list = ['b', 'c', 't', 'e']
    value = 'c'
    assert binary_search(list, value) == 1 

def test_binary_search_value_not_listed():
    list = [1, 2, 3, 7, 8]
    value = 5
    assert binary_search(list, value) is None