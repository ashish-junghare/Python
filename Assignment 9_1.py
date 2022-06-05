from sys import *
import os


def DirectoryWatcher(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:

        for foldername, subfolder, filname in os.walk(path):

            for subf in subfolder:
                pass

            for filen in filname:
                pass

            print('File exist')

    else:
        print("Invalid Path")


def main():
    print("---- Marvellous Infosystems Project-----")

    print("Application name : " + argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName File existance in system")
        exit()

    try:
        DirectoryWatcher(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input : ",ValueError)

    except Exception:
        print("Error : Invalid input: ",Exception)


if __name__ == "__main__":
    main()
