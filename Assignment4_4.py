import functools
'''def EvenCheck(no1):
    if no1%2==0:
        return True
    else:
        return False'''
EvenCheck = lambda no1:no1%2==0

'''def square(no1):
    square = no1*no1
    return square'''
square = lambda no1:no1*no1

'''def sum(a, b):
    return (a + b)'''
sum = lambda a,b:a+b


def main():
    list1 = []
    size = int(input("Enter size of list - "))
    for i in range(size):
        no1 = int(input("Enter the element: "))
        list1.append(no1)
    print("Your list is: ", list1)

    data1 = list(filter(EvenCheck, list1))
    print("your filtered list is: ", data1)

    data2 = list(map(square, data1))
    print("your mapping list is: ", data2)

    data3 = functools.reduce(sum, data2)
    print("your reduce data is: ", data3)


if __name__ == "__main__":
    main()