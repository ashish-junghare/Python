

def CheckEven(iNo):
   if((iNo%2)==0):
      return True
   else:
      return False

def main():
   
   iValue=0
   bRet=False

   iValue=int(input("Enter any number to chech whether it is even or odd number: \n"))

   bRet=CheckEven(iValue)
   
   if (bRet==True):
      print("It is even number\n")
   else:
      print("It is odd number\n")

if __name__=="__main__":
   main()