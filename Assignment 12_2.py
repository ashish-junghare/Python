import psutil
import os
import time
import smtplib
import schedule
from sys import *



def ProcessLog(x,log_dir="Process Display"):
    listprocess = []


    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=["pid", "name", "username"])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        if x in listprocess:
        	print("Process is running")
        else:
        	print("Process is not running")


def main():
    print("Python automation and machine learning")
    print("Process monitor with memory usage")

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to show running process into log file after certain time ")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName_show_running_process_into_log_file")
        exit()

    try:
    	listprocess=ProcessLog(argv[1])
        
    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()
