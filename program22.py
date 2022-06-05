#program to display summation of n number

def Summation(iNo):

   iSum=0
   
   if(iNo<0):
      iNo=-iNo
   
   for i in range(iNo+1):
      iSum=iSum+i
   
   return iSum


def main():
   
   iRet=0
   
   iValue=int(input("Enter any number\n"))

   iRet=Summation(iValue)
   print("Addition is: \n",iRet)


if __name__=="__main__":
   main()