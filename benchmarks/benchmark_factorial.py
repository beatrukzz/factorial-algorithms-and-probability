import time
from factorial_toolkit.factorial import (
    factorial,
    factorial_recursive,
    factorial_memo,
)

N = 500

def run_benchmark(func, name, n):
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    print(
        f"{name:<20} | result digits: {len(str(result)):<5} | time: {end - start:.6f}s"
    )

if __name__ == "__main__":
    print("Benchmarking factorials\n")

    run_benchmark(factorial, "iterative (500)", 500)
    run_benchmark(factorial_recursive, "recursive (100)", 100)
    run_benchmark(factorial_memo, "memoized (100)", 100)
