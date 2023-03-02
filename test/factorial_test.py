from src.factorial import factorial

def test_factorial_succesfully():
    value = 3
    result = factorial(value)
    assert result == 6

def test_factorial_succesfully():
    value = 5
    result = factorial(value)
    assert result == 120