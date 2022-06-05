#Check whether number is armstrong or not


def ChkArmstrong(iNo):
   iCnt=0
   iTemp=0
   iSum=0
   if(iNo<0):
      iNo=-iNo
   
   iTemp=iNo
   while iNo!=0:
      iCnt+=1
      iNo=iNo//10

   iNo=iTemp
   while iNo!=0:
      iMult=1
      i=0
      iDigit=iNo%10
      for i in range(iCnt):
         iMult=iMult*iDigit
      iSum=iSum+iMult
      iNo=iNo//10

   if(iSum==iTemp):
      return True
   else:
      return False

   



def main():
   bRet=False
   iValue=int(input("Enter number to check armstrong number: "))
   bRet=ChkArmstrong(iValue)
   if(bRet==True):
      print(iValue,"is armstrong number")
   else:
      print(iValue,"is not armstrong number")


if __name__=="__main__":
   main()
