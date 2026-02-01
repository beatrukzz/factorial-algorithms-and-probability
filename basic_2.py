def factorial(n: int) -> int:
    """
    Returns the factorial of a non-negative integer n.

4    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main():
    """
    Main function to handle user input and output.
    """
    try:
        user_input = input("Pick a number to find its factorial: ")
        number = int(user_input)

        answer = factorial(number)
        print(f"The factorial of {number} is {answer}")

    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
