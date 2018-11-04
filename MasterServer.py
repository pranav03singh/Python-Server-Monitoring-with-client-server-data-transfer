import socket
import pickle
import json


s = socket.socket()
#host = socket.gethostname()
host='127.0.0.1'
print(" server will start on host : ", host)
port = 55551
s.bind((host, port))
print("")
print(" Server done binding to host and port successfully")
print("")
print("Server is waiting for incoming connections")
print("")
s.listen(1)
conn, addr = s.accept()
print(addr, " Has connected to the server and is now online ...")

UserInput=input(str("Type 'Start' to Start Client to send data"))

message=pickle.dumps(UserInput)
conn.send(message)

while 1:
    incoming_message = conn.recv(1024)
    a=(pickle.loads(incoming_message))

    print(json.loads(a))



