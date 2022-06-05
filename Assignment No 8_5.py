import threading
import time


def thread1(value1):
    for i in range(value1):
        print(i)


def thread2(value2):
    for i in range(value2):
        value2 = value2 - 1
        print(value2)
def main():
    no=50
    Start_time = time.time()
    p1 = threading.Thread(target=thread1, args=(no,))
    p1.start()
    p1.join()

    p2 = threading.Thread(target=thread2, args=(no,))
    p2.start()
    p2.join()

    End_time = time.time()
    Requird_time = End_time - Start_time

    print("Required time for application is: ", Requird_time)
    print("End of appliaction")


if __name__ == "__main__":
    main()
