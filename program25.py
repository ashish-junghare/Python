
"""
35 = fail
50 = pass
60 = second
70 = first
70+ = Distinct 
"""



def DisplayPass(fMarks):
      if((fMarks>0.0) and (fMarks<35.0)):
         print("You are fail\n")
      elif((fMarks>=35.0) and (fMarks<50.0)):
         print("You are in pass class\n")
      elif((fMarks>=50.0) and (fMarks<60.0)):
         print("You are in second class\n")
      elif((fMarks>=60.0) and (fMarks<70.0)):
         print("You are in first class\n")
      elif((fMarks>=70.0) and (fMarks<100.0)):
         print("You are in first class with distinction\n")
      else:
         print("Invalid output\n")

def main():
   iValue=0
   iValue=int(input("Enter your percentage: \n"))
   DisplayPass(iValue)



if __name__=="__main__":
   main()