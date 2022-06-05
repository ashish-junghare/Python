from sys import *
import os

def ext(path):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    
    if exists:
        
        for foldername, subfolder, filname in os.walk(path):
            pass

            for subf in subfolder:
                pass

            for filen in filname:
                a=filen.split('.')
                
                if a[1]==argv[2][1:]:
                    print("file with extention {} is:  {} ".format(argv[2],filen))
            print(' ')

    else:
        print("Invalid Path")

def main():
    print("---- Assignment 10-----")

    print("Application name : " +argv[0])

    if (len(argv) != 3):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory to find same extension")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory_find_same_extension")
        exit()

    try:
        ext(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")

if __name__ == "__main__":
    main()
