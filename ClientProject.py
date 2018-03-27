import socket

IP= "192.168.2.2"
port = 5000
Message="this shows information sending via TPS connection"

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((IP, port))
client.send(Message.encode())
returned=client.recv(1024).decode()
print (returned)
client.close()
