class Numbers:
    def __init__(self, value):
        self.value = value


    def ChkPrime(self, value):
        for i in range(2, value):
            if value % i == 0:
                print(False)
                break
        else:
            print(True)

    def ChkPerfect(self, value):
        sum = 0
        for i in range(1, value):
            if value % i == 0:
                sum = sum + i
        if sum == value:
            print(True)
        else:
            print(False)


    def SumFactors(self, value):
        sum=0
        for i in range(1, value):
            if value % i == 0:
                sum = sum + i
        print("Sum of factors is: ", sum)

    def Factors(self, value):
        for i in range(1, value):
            if value % i == 0:
                print("factors is: ", i, end=" ")


def main():
    obj1 = Numbers(10)
    obj1.ChkPrime(10)
    obj1.ChkPerfect(10)
    obj1.SumFactors(10)
    obj1.Factors(10)


if __name__ == "__main__":
    main()