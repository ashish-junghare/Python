from sys import *
import os

def createf(name):


    fd1= open(name,"x")
    fd = open('ABC.txt', "r")
    data = fd.read()

    fd1.write(data)
    fd.close()
    print("Your data moved in new file")


def main():
    print("---- Assignment No 9 -----")

    print("Application name : " + argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to copy data from one file to another")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName copy data from one file to another")
        exit()

    try:
        createf(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input ; ",ValueError)

    except Exception:
        print("Error : Invalid input: ",Exception)


if __name__ == "__main__":
    main()
