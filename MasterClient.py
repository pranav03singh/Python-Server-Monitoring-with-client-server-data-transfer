import socket
import pickle
import psutil
import sys
import time
import json

data={}
s = socket.socket()
#host = input(str("Please enter the hostname of the server : "))
host='127.0.0.1'
port = 55551
s.connect((host, port))
print(" Connected to the server")S
incoming_message = s.recv(1024)

Message=pickle.loads(incoming_message)

while Message =='Start' or 'start' or 'START':
    ram = psutil.virtual_memory().percent
    cpupercent = psutil.cpu_percent()
    data[host]={
        'time': str(time.ctime()),
        'ram': ram,
        'cpu': cpupercent
    }
    strMessage=json.dumps(data)
    strMessage=pickle.dumps(strMessage)
    s.send(strMessage)

    time.sleep(5.0)

