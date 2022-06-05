import psutil
import os
import time
import smtplib
import schedule
from sys import *
from urllib.request import urlopen
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart



def ProcessLog(log_dir="Demo"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-" * 80
    log_path = os.path.join(log_dir, "ProcessLog%s.log" % (time.ctime()))
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Ashish Junghare Machine: " + time.ctime() + "\n")
    f.write(separator + "\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=["pid", "name", "username"])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)

        print("Log File is succefully generated at loacation: ", log_path)


def main():
    print("Python automation and machine learning")
    print("Process monitor with memory usage")

    if (len(argv) != 1):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to show running process into log file after certain time ")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName_show_running_process_into_log_file")
        exit()

    try:
        listprocess=ProcessLog()
    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()
