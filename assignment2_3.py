def fact(value1):
    factorial = 1
    for i in range(1, value1 + 1):
        factorial = factorial * i
    return (factorial)


def main():
    no1 = int(input("Enter any number to get it's factorial: "))
    ret = fact(no1)

    print("factorial of number is ", ret)


if __name__ == "__main__":
    main()