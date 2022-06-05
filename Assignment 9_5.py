from sys import *
import os


def freqn(x, y):
    fname = x
    word = y
    k = 0

    with open(fname, 'r') as f:
        for line in f:
            words = line.split()
            for i in words:
                if (i == word):
                    k = k + 1
    print("Frequency of {} given argument is: {}".format(y, k))


def main():
    print("----- Assignment No.9----")

    print("Application name : " + argv[0])

    if (len(argv) != 3):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to find frequency of word in file")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName find frequency of word in file")
        exit()

    try:
        freqn(argv[1], argv[2])


    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()
