#program to display summation of n number

def Check(iNo):
   if((iNo%3)==0 and (iNo%5)==0):
      return True
   else:
      return False


def main():
   
   iValue=0
   bRet=False

   iValue=int(input("Entern number: "))

   bRet=Check(iValue)
   
   if (bRet==True):
      print(iValue,"is divisible by 3 and 5\n")
   else:
      print(iValue,"is not divisible by 3 and 5\n")

if __name__=="__main__":
   main()