# tests/test_factorial.py
import pytest
from src.factorial import factorial, factorial_recursive, factorial_memo

def test_zero():
    assert factorial(0) == 1
    assert factorial_recursive(0) == 1
    assert factorial_memo(0) == 1

def test_one():
    assert factorial(1) == 1
    assert factorial_recursive(1) == 1
    assert factorial_memo(1) == 1

def test_small_numbers():
    for i, expected in [(2, 2), (3, 6), (4, 24), (5, 120)]:
        assert factorial(i) == expected
        assert factorial_recursive(i) == expected
        assert factorial_memo(i) == expected

def test_large_number():
    expected = 2432902008176640000  # 20!
    assert factorial(20) == expected
    assert factorial_recursive(20) == expected
    assert factorial_memo(20) == expected

def test_type_error():
    with pytest.raises(TypeError):
        factorial(3.5)
    with pytest.raises(TypeError):
        factorial_recursive("5")
    with pytest.raises(TypeError):
        factorial_memo([5])

def test_value_error():
    with pytest.raises(ValueError):
        factorial(-3)
    with pytest.raises(ValueError):
        factorial_recursive(-10)
    with pytest.raises(ValueError):
        factorial_memo(-1)
