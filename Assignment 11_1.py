from sys import *
import os
import hashlib

def checksumx(path):

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
                print(filen)
            
            with open(filen, 'rb') as open_file:
                data = open_file.read()
                hasher = hashlib.md5(data).hexdigest()
            print("CheckSum for {} is {}".format(file,hasher))



def main():
    print("----- Assignment No.11----")

    print("Application name : " + argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to display checksum")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName_display_checksum")
        exit()

    try:
        checksumx(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()
