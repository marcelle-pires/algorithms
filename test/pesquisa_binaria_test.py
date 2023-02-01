from src.binary_search import binary_search 

def test_binary_search_sucessfully():
    list = [1, 2, 3, 7, 8]
    valor = 2
    assert binary_search(list, valor) == 1 

def test_binary_search_value_not_listed():
    list = [1, 2, 3, 7, 8]
    valor = 5
    assert binary_search(list, valor) is None