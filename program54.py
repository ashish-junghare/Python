#palindrome number

def ChkPallindrome(iNo):
   iDigit=0
   iRev=0
   iCopy=0

   if(iNo<0):
      iNo=-iNo

   iCopy=iNo

   while(iNo>=1):
      iDigit=iNo%10
      iRev=iRev*10+iDigit
      iNo=iNo//10

   if(iCopy==iRev):
      return True
   else:
      return False
   



def main():
   bRet=False
   iValue1=int(input("Enter any number: \n"))
   bRet=ChkPallindrome(iValue1)
   if(bRet==True):
      print("It is pallindrome number")
   else:
      print("It is not a pallindrome number")
   


if __name__=="__main__":
   main()