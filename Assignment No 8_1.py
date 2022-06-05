import threading
import time

def Check_Even(no):
    if no == 0:
        return 'Zero'
    elif no % 2 == 0:
        print("Even number is", no)



def Check_Odd(no):
    if no == 0:
        return 'zero'
    elif no % 2 != 0:
        print("Odd number is", no)



def main():
    Start_time = time.time()
    for n in range (10):
        p1 = threading.Thread(target=Check_Even, args= (n,))
        p1.start()

    for n in range(10):
        p2 = threading.Thread(target=Check_Odd, args= (n,))
        p2.start()

    p1.join()
    p2.join()

    End_time = time.time()
    Requird_time = End_time-Start_time

    print("Required time for application is: ", Requird_time)

if __name__=="__main__":
    main()
