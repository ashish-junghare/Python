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


def is_connected():
    try:
        urlopen('https://www.google.co.in/')
        return True
    except:
        return False


def MailSender(filename, time):
    try:
        fromaddr = "junghsham@gmail.com"
        toaddr = "ashishj.academics@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr

        msg['To'] = toaddr

        body = '''

    	hello %s,

    	Please find attached log file of processes in Ashish Junghare's machine
    	log file created at: %s

        ---This is auto generated mail----

        Thanks & regards.
         Ashish Junghare
         ''' % (toaddr, time)

        Subject = '''
                Ashish Junghare's  machine log process report generated at: %s
                '''%(time)
        msg['Subject'] = Subject
        msg.attach(MIMEText(body, 'plain'))
        attachment = open(filename, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment;filename=%s" % filename)
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com:587')
        s.starttls()
        s.login(fromaddr, 'sham@123')
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()
        print("Log file succefully sent through mail")
    except:
        print("Mail not sent")


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

    connected = is_connected()
    if connected:
        starttime = time.time()
        MailSender(log_path, time.ctime())
        endtime = time.time()
        print("Took %s seconds to send mail" % (endtime - starttime))

    else:
        print("There is no Connection")


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
        schedule.every(int(argv[1])).minutes.do(ProcessLog)

        while True:
            schedule.run_pending()

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()
