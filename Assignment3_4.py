def freq(value1):
    list1 = []
    freq = {}
    for i in range(1, value1 + 1):
        no2 = int(input("Enter elements in list: "))
        list1.append(no2)
    for items in list1:
        freq[items] = list1.count(items)
    print(list1)

    no2 = int(input("Enter element to search: "))

    for key, value in freq.items():
        if no2==freq.items():
            break
        return(value)


def main():
    no1 = int(input("Enter size of elements: "))
    ret = freq(no1)
    print("frequency of elements in list is ", ret)


if __name__ == "__main__":
    main()