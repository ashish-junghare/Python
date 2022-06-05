def max(value1):
    list1 = []
    for i in range(1, value1 + 1):
        no2 = int(input("Enter elements in list: "))
        list1.append(no2)
    print(list1)
    list1.sort()
    value2=list1[-1]
    return (value2)


def main():
    no1 = int(input("Enter size of elements: "))
    ret = max(no1)
    print("Smallest number of elements in list is ",ret)


if __name__ == "__main__":
    main()