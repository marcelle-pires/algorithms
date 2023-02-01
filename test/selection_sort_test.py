from src.selection_sort import selection_sort
from src.selection_sort import find_least 

def test_find_least_sucessfully():
    array = [30, 20, 10, 4, 6, 2]
    expected_result_array = 5

    index_least = find_least(array)

    assert index_least == expected_result_array

def test_selection_sort_sucessfully():
    array = [30, 20, 10, 4, 6, 2]
    expected_result_array = [2, 4, 6, 10, 20, 30]

    result = selection_sort(array)

    assert result == expected_result_array

def test_selection_sort_sucessfully_with_char_values():
    array = ['a', 's', 'l']
    expected_result_array = ['a', 'l', 's']

    result = selection_sort(array)

    assert result == expected_result_array
