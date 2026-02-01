def num_factorials(num):
    if num < 0:
        return None
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


try:
    num = int(input("pick a number to find its factorial: "))
except ValueError:
    print("this is an invalid character")
else:
    if num < 0:
        print("that is an invalid number")
    elif num == 0:
        print("the factorial of 0 is 1")
    else:
        print(f"the factorial of your number is: {num_factorials(num)}")
