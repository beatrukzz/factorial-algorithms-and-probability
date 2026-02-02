import argparse

from factorial_toolkit.factorial import (
    factorial,
    factorial_recursive,
    factorial_memo,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compute factorials using different algorithms"
    )

    parser.add_argument(
        "n",
        type=int,
        help="Non-negative integer to compute the factorial of",
    )

    parser.add_argument(
        "--method",
        choices=["iterative", "recursive", "memo"],
        default="iterative",
        help="Algorithm to use",
    )

    args = parser.parse_args()

    if args.method == "iterative":
        result = factorial(args.n)
    elif args.method == "recursive":
        result = factorial_recursive(args.n)
    else:
        result = factorial_memo(args.n)

    print(result)


if __name__ == "__main__":
    main()
    