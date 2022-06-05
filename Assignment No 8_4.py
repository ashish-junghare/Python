import threading
import time


def small(z):
    count1=0
    for i in z:
        if i.isupper():
            count1+=1
    print("Number of small char is: ",count1)


def capital(z):
    count2=0
    for i in z:
        if i.islower():
            count2+=1
    print("Number of Upper char is: ",count2)

def digit(z):
    count3=0
    for i in z:
        if i.isdigit():
            count3+=1
    print("Number of Digit is: ",count3)


def main():
    str1 = input("Enter your string: ")

    Start_time = time.time()
    p1 = threading.Thread(target=small, args=(str1,))
    p2 = threading.Thread(target=capital, args=(str1,))
    p3 = threading.Thread(target=digit, args=(str1,))
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    End_time = time.time()
    Requird_time = End_time - Start_time

    print("Required time for application is: ", Requird_time)
    print("End of appliaction")


if __name__ == "__main__":
    main()
