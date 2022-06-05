# import Marvellous
# from Marvellous import *
import Marvellous as M
import Infosystems

def main():
    print("Inside module :",__name__)
    no1 = int(input("Enter first number : "))       # 10
    no2 = int(input("Enter second number : "))  # 11
    
    ret = M.Addition(no1, no2)    # Addition(10,11)
    print("Addition is : ",ret)
    
    ret = Infosystems.Substraction(no1,no2)
    print("Substraction is :",ret)
    
if __name__ == "__main__":
    main()
