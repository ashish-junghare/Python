from sys import *
import os
from hashlib import *

def similar_file(path,new_path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    if exists:
        os.mkdir(new_path)
        flag = os.path.isabs(new_path)
        if flag == False:
            temppath = os.path.abspath(new_path)
        for foldername ,subfolder,filename in os.walk(path):
            pass
            for subf in subfolder:
                pass
                for file in filename:
                    pass
                
                with open(file, 'rb') as file_to_check:
                    data = file_to_check.read()
                    md5_returned = hashlib.md5(data).hexdigest()
                        
                print(file,md5_returned)
                
                src = os.path.join(foldername, file)
                dst = os.path.join(temppath,file)
                copyfile(src, dst)
                    
    print("File moved in "+argv[2],"files....")


def main():
    print("----- Assignment No.11----")

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
