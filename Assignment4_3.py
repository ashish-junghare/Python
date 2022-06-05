import functools
'''def ifx(no1):
    if no1 >= 70 and no1 <= 90:
        return True
    else:
        return False'''
ifx = lambda no1:no1 >= 70 and no1 <= 90

'''def add(no1):
    sum = 0
    sum = no1 + 10
    return sum'''
add = lambda no1:no1+10

'''def product(a, b):
    return (a * b)'''
product = lambda a,b:a*b


def main():
    list1 = []
    size = int(input("Enter size of list - "))
    for i in range(size):
        no1 = int(input("Enter the element: "))
        list1.append(no1)
    print("Your list is: ", list1)

    data1 = list(filter(ifx, list1))
    print("your filtered list is: ", data1)

    data2 = list(map(add, data1))
    print("your mapping list is: ", data2)

    data3 = functools.reduce(product, data2)
    print("your reduce data is: ", data3)


if __name__ == "__main__":
    main()