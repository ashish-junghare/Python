from sys import *
import os
import hashlib

def similar_file(x,y):
    
    with open(x, 'rb') as file_to_check:
        data = file_to_check.read()
        md5_returned1 = hashlib.md5(data).hexdigest()

    with open(y, 'rb') as file_to_check:
        data = file_to_check.read()
        md5_returned2 = hashlib.md5(data).hexdigest()

    if md5_returned1 == md5_returned2:
        print(" Data in both files matched.")
    else:
        print(" Data in both files not matched.")

def main():
    print("----- Assignment No.9----")

    print("Application name : " + argv[0])

    if (len(argv) != 3):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to compare data content in two files")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName compare data content in two files")
        exit()

    try:
        similar_file(argv[1],argv[2])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()
