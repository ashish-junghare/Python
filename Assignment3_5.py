import ChkPrime as MarvellousNum

def main():
    no1 = int(input("Enter size of elements: "))
    list1 = []
    for i in range(1, no1 + 1):
        no2 = int(input("Enter elements in list: "))
        list1.append(no2)
    ret=MarvellousNum.ChkPrime(*list1)
    print(ret)


if __name__ == "__main__":
    main()