import os
import platform
import ftplib

myCmd = os.popen('python project-ui.py > log.txt').read()
print(myCmd)

myCmd = os.popen('python check.py >> log.txt').read()
print(myCmd)

myCmd = os.popen('python project-ui.py').read()
print(myCmd)

myCmd = os.popen('python check.py').read()
print(myCmd)

session = ftplib.FTP('idp-log.do.am','8idp-log','Password321')
file = open('log.txt','rb')                  # file to send
session.storbinary('STOR /log/log.txt', file)     # send the file
file.close()                                    # close file and FTP
session.quit()
