class circle:
    PI = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumferance = 0.0

    def accept(self):
        self.radius = float(input("Enter value of radius: "))

    def calulatearea(self):
        self.area = self.PI * self.radius * self.radius

    def calculatecircumference(self):
        self.circumferance = 2 * self.PI * self.radius

    def Display(self):
        print("Radius is: ",self.radius)
        print("Area is: ",self.area)
        print("circumferance is: ",self.circumferance)


def main():
    obj1 = circle()
    obj1.accept()
    obj1.calulatearea()
    obj1.calculatecircumference()
    obj1.Display()


if __name__ == "__main__":
    main()