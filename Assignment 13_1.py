import os
import smtplib
import time
from sys import *
from urllib.request import urlopen
import fnmatch
import hashlib
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

    	Please find attached log file of deleting duplicate files in Ashish Junghare's machine

    	log file created at: %s

    	Total number of files scanned: 

    	Total number of duplicate files found:

        ---This is auto generated mail----

        Thanks & regards.
         Ashish Junghare
         ''' % (toaddr, time)

        Subject = '''
                Ashish Junghare's  machine log file of deleting duplicate files: %s
                ''' % (time)
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


def DeleteFile(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    icnt = 0
    if len(results) > 0:
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    os.remove(subresult)
            icnt = 0
    else:
        ("No Duplicate File Found....")


def hashfile(path, blocksize=1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def findDup(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)
    exists = os.path.isdir(path)
    dups = {}
    if exists:
        for dirName, subdirs, filelist in os.walk(path):
            for filen in filelist:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups
    else:
        ("Invalid path")


def printResult(dict1, log_dir="Marvellous"):
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass


    separator = "-" * 80
    log_path = os.path.join(log_dir, "DupFiles%s.log" % (time.ctime()))
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Ashish Junghare Machine Dup found: " + time.ctime() + "\n")
    f.write(separator + "\n")
    f.write("\n")

    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    if len(results) > 0:
        print("Duplicate Found: ")
        print("The following files are duplicate: ")
        for result in results:
            for subresult in result:
                f.write('\t\t%s' % subresult)


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

    # try:

    starttime = time.time()
    arr = {}
    arr = findDup(argv[1])
    printResult(arr)
    DeleteFile(arr)
    endtime = time.time()
    required_time = endtime - starttime
    print("Took %s time to process" % (required_time))



'''except ValueError:
    print("Error : Invalid datatype of input")

except Exception:
    print("Error : Invalid input")'''

if __name__ == "__main__":
    main()
