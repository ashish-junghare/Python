from sys import *
import os
import hashlib
import logging
import datetime


def DirectoryWatcher(path):
    dups={}
    logging.basicConfig(filename="log.txt",filemode='w')
    logging.debug('Same file names: ')
    
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    
    if exists:
        
        for foldername, subfolder, filname in os.walk(path):
            pass

            for subf in subfolder:
                pass

            for file in filname:
                print("File inside "+foldername+"is : "+file)
                with open(file,'rb') as fd:
                    hasher = hashlib.md5()
                    buf = fd.read()
                    while len(buf)>0:
                        hasher.update(buf)
                        buf = fd.read()
                        fd.close()
                        a1=hasher.hexdigest()
                        if a1 in dups:
                            dups[a1].append(path)
                        else:
                            dups[file] = [path]
                            a2=dups
                        
                    for key in dups.keys():
                        if key in dups:
                            dups1[key] = dups1[key] + dups2[key]
                        else:
                            dups1[key] = dups1[key]
                        results = list(filter(lambda x: len(x) > 1, dups1.values()))
                        if len(results) > 0:
                            logging.debug(key)
                            



def main():
    print("---- Assignment 10-----")

    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to delete dupliacte files and display application time ")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_delete_dupliacte_files_and_display_application_time")
        exit()

    Start_time=datetime.datetime.now()
    try:
        DirectoryWatcher(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")

    End_time=datetime.datetime.now()
    
    required_time=End_time-Start_time
    
    logging.debug("Time required for application: ",required_time)


if __name__=="__main__":
    main()