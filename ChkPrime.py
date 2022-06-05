def ChkPrime(*list2):

    list3 = []

    def prime(value1):
        if value1 > 1:
            for i in range(2, value1):
                if (value1 % i) == 0:
                    print("It is not a prime value")
                    break
            else:
                print("It is a prime value")

        else:
            print("It is not a prime value")
            return ()

    for i in range(len(list2)+1):
        if i % 2 != 0:
            list3.append(i)
        else:
            continue
    print(list3)
    sum = 0
    for i in range(len(list3) + 1):
        sum = sum + int(i)
    print(sum)