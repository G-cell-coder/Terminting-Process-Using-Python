import pysftp
import os
import sys
import signal
from easygui import passwordbox
import psutil
import socket


process_name = "pycharm64"
pid = None

for proc in psutil.process_iter():
    if process_name in proc.name():
       pid = proc.pid

pwd = passwordbox("Enter the PASSWORD:")
HOST = socket.gethostbyname(socket.gethostname())

dr = pysftp.Connection(host=HOST, username="guhan_s", password=pwd)

data = dr.listdir()
print(signal.SIGTERM)

print(pid)
os.kill(pid, signal.SIGINT)


for i in data:
    print(i)