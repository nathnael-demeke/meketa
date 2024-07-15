import socket 
import json 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect(("localhost", 132))
message = {"Action": "Approve", "DriverDirectory" : "D:\\"}
server.send(json.dumps(message).encode("utf-8"))