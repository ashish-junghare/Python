class Demo:
    value = 10
	def __init__(self, no1, no2):
        self.c = no1
        self.d = no2


    def fun(self):
        print(self.c)
        print(self.d)


    def gun(self):
        print(self.c)
        print(self.d)
		
def main():
    value1=int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))
    ret=Demo(value1,value2)
    obj1 = Demo(11, 21)
    obj2 = Demo(51, 101)
    obj1.fun()
    obj2.fun()
    obj1.gun()
    obj2.gun()


if __name__ == "__main__":
    main()