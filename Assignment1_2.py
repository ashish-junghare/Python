def chknum(value1):
    if value1 % 2 ==0:
        print("value1 is even number")
    else:
        print("value1 is odd number")


    return (value1)


def main():
    no1 = int(input("Enter your first Number"))

    ret = chknum(no1)

    print(ret)


if __name__ == "__main__":
    main()