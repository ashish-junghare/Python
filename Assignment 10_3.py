from sys import *
from shutil import copyfile
import os


def CopyFile(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    if exists:
        os.mkdir(argv[2])
        flag = os.path.isabs(argv[2])
        if flag == False:
            temppath = os.path.abspath(argv[2])
        for foldername ,subfolder,filename in os.walk(path):
            pass
            for subf in subfolder:
                pass
                for file in filename:
                    src = os.path.join(foldername, file)
                    dst = os.path.join(temppath,file)
                    copyfile(src, dst)
                    
            print("File moved in "+argv[2],"files....")



    else:
        print("invalid path")


def main():
    print("---- Assignment 10-----")

    print("Application name : " +argv[0])

    if (len(argv) != 3):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to copy files")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName_copy_files")

    try:
        CopyFile(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")



if __name__=="__main__":
    main()