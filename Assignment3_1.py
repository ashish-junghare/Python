def add(value1):
    list1 = []
    for i in range(1, value1 + 1):
        no2 = int(input("Enter elements in list: "))
        list1.append(no2)
    total = sum(list1)
    return total


def main():
    no1 = int(input("Enter size of elements: "))
    ret = add(no1)
    print("Addition os elements in list", ret)


if __name__ == "__main__":
    main()