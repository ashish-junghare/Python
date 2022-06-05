import threading
import time

def Even_Factor(value1):
    add1 = 0
    for i in value1:
        if i % 2 == 0:
            add1 = add1 + i
    print("Addition of even factors: ", add1)

def Odd_Factor(value2):
    add=0
    for i in value2:
        if i % 2 != 0:
            add = add + i
    print("Addition of odd factors: ", add)

def main():
    no=int(input("Enter any integer: "))
    Start_time = time.time()

    factor = []
    for n in range(1, no+1):
        if no % n == 0:
            factor.append(n)
    print(factor)

    p1 = threading.Thread(target=Even_Factor, args=(factor,))
    p2 = threading.Thread(target=Odd_Factor, args=(factor,))
    p1.start()
    p2.start()


    p1.join()
    p2.join()

    End_time = time.time()
    Requird_time = End_time-Start_time

    print("Required time for application is: ", Requird_time)
    print("End of appliaction")

if __name__=="__main__":
    main()
