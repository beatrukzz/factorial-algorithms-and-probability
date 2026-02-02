import time
from factorial_toolkit.factorial import (
    factorial,
    factorial_recursive,
    factorial_memo,
)

N = 500

def run_benchmark(func, name):
    start = time.perf_counter()
    result = func(N)
    end = time.perf_counter()
    print(f"{name:<20} | result digits: {len(str(result)):<5} | time: {end - start:.6f}s")

if __name__ == "__main__":
    print(f"Benchmarking factorial({N})\n")

    run_benchmark(factorial, "iterative")
    run_benchmark(factorial_recursive, "recursive")
    run_benchmark(factorial_memo, "memoized")
