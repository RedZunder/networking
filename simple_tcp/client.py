import socket

HOST=socket.gethostbyname(socket.gethostname())     #same as server private IP since it's all in the same machine
PORT=6969

#TCP socket
socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#send TCP request
socket.connect((HOST,PORT))
socket.send(f"I am a client".encode('utf-8'))

print(f"Server said: {socket.recv(1024).decode('utf-8')}")

