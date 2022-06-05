#Find largest

def ChkIndex(ls1,iLength):
   iMax=ls1[0]
   for i in range(iLength):
      if(iMax<ls1[i]):
         iMax=ls1[i]

   return iMax

def main():
   list1=[]
   iSize=int(input("Enter the size of list: "))
   for i in range(iSize):
      iNo=int(input("Enter element: "))
      list1.append(iNo)
   

   iRet=ChkIndex(list1,iSize)
   print(iRet)

if __name__=="__main__":
   main()
