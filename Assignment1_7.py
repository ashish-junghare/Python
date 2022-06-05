def check(x):
    if x %5 == 0:
        print("True")
    else :
        print("False")
    return (x)


def main():
    no1 = int(input("Enter number"))

    ret = check(no1)


if __name__ == "__main__":
    main()