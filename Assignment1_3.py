def Add(value1,value2):
    i = int(value1)+int(value2)
    return (i)

def main():
    no1 = input("Enter your first Number")
    no2 = input("Enter your second Number")
    ret = Add(no1,no2)

    print(ret)


if __name__ == "__main__":
    main()