import socket

IP= "192.168.2.2"
port = 5000

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('',port))
server.listen(1)
print ('the server is ready to recieve')
while 1:
    connectionSocket, addr = server.accept()

    sentence=connectionSocket.recv(1024).decode()
    print (sentence)
    connectionSocket.send('information Recieved'.encode())
