# src/factorial.py
from functools import lru_cache

def factorial(n: int) -> int:
    """
    Iterative factorial function.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n: int) -> int:
    """
    Recursive factorial function.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

@lru_cache(maxsize=None)
def factorial_memo(n: int) -> int:
    """
    Memoized recursive factorial function.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial_memo(n - 1)
