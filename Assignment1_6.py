def check(x):
    if x > 0:
        print("Given number is positive")
    elif x < 0:
        print("Given number is negative")
    else :
        print("Given number is zero")
    return (x)


def main():
    no1 = int(input("Enter number"))

    ret = check(no1)


if __name__ == "__main__":
    main()