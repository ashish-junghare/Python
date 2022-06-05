#Check first occurance

def ChkIndex(ls1,iLength,iValue1):
   bFlag=False
   for i in range(iLength):
      if(iValue1==ls1[i]):
         bFlag=True
         break
   if(bFlag==False):
      return -1
   else:
      return i



def main():
   list1=[]
   iSize=int(input("Enter the size of list: "))
   for i in range(iSize):
      iNo=int(input("Enter element: "))
      list1.append(iNo)
   
   iNo1=int(input("Enter element to search: "))

   iRet=ChkIndex(list1,iSize,iNo1)
   print(iRet)

if __name__=="__main__":
   main()
