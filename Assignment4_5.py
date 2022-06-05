import functools
def PrimeCheck(no1):
    for i in range(2,no1):
        if no1%i==0:
            return False
    else:
        return True

def mult(no1):
    mult = no1*2
    return mult

def max1(a, b):
    return max(a , b)


def main():
    list1 = []
    size = int(input("Enter size of list - "))
    for i in range(size):
        no1 = int(input("Enter the element: "))
        list1.append(no1)
    print("Your list is: ", list1)

    data1 = list(filter(PrimeCheck, list1))
    print("your filtered list is: ", data1)

    data2 = list(map(mult, data1))
    print("your mapping list is: ", data2)

    data3 = functools.reduce(max1, data2)
    print("your reduce data is: ", data3)


if __name__ == "__main__":
    main()