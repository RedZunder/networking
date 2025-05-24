import socket

HOST = socket.gethostbyname(socket.gethostname())       #192.168.1.15
PORT = 6969



# create TCP socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#lock IP and port for the socket
server.bind((HOST,PORT))

server.listen(5)        #max 5 connections without accepting


while True:
    comm_socket, addss = server.accept()        #info of the client - new socket for each client
    print(f'IP: {addss}')
    message=comm_socket.recv(1024).decode('utf-8')     #bytes received to string
    print(f'Message is: {message}')
    comm_socket.send(f"I am a server".encode('utf-8'))
    comm_socket.close()
    print(f'Connection with {addss} finished')




