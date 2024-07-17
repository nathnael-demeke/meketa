import socket 
import json 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect(("localhost", 132))
message = {"Action": "Disapprove", "DriverDirectory" : "C:\\all\\R.file"}
server.send(json.dumps(message).encode("utf-8"))
server.close()