import socket
import sys
HOST = ""    
PORT = sys.argv[1]             
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))
stringa=sys.argv[2]
socket.send(stringa.encode())
stringa2 = socket.recv(1024).decode()
print ('Server::. \t'+stringa2)
stringa2 = socket.recv(1024).decode()
print ('Server::. \t'+stringa2)
socket.close()