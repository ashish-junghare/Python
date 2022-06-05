class Arithematic:
    def __init__(self):
        self.no1 = 0
        self.no2 = 0

    def accept(self):
        print("Enter first number : ")
        self.no1 = int(input())
        print("Enter second number : ")
        self.no2 = int(input())

    def Addition(self):
        ans=0
        ans = self.no1 + self.no2
        return ans

    def substraction(self):
        sub = 0
        sub = self.no1 - self.no2
        return sub

    def multiplication(self):
        mul = 0
        mul = self.no1 * self.no2
        return mul

    def division(self):
        div = 0
        div = self.no1 / self.no2
        return div


def main():
    obj1 = Arithematic()
    obj1.accept()

    ret = obj1.Addition()
    print("Addition is  : ", ret)

    ret = obj1.substraction()
    print("substraction is: ", ret)

    ret = obj1.multiplication()
    print("multiplication is: ", ret)

    ret = obj1.division()
    print("division is: ", ret)


if __name__ == "__main__":
    main()