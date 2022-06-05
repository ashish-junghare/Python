from sys import *
import os

def fext(paths):

    flag = os.path.isabs(paths)
    if flag == False:
        path = os.path.abspath(paths)

    exists = os.path.isdir(paths)
    
    if exists:
        
        for foldername, subfolder, filname in os.walk(path):
            pass

            for subf in subfolder:
                pass

            for filen in filname:
                a=filen.split('.')
                if a[1]==argv[2][1:]:
                    pre = os.path.splitext(filen)[0]
                    old_path = os.path.join(foldername, filen)
                    new_name = os.path.join(foldername, pre + argv[3])
                    os.rename(old_path, new_name)
            print("Renaming Successful...")
                    
                    
            

    else:
        print("Invalid Path")

def main():
    print("---- Assignment 10-----")

    print("Application name : " +argv[0])

    if (len(argv) != 3):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to rename file extension")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_rename_file_extension")
        exit()

    try:
        fext(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")

if __name__ == "__main__":
    main()
