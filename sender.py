import socket

IP= "192.168.2.8"
port = 5000
Message="test".encode()

sen=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
i=0
while i<10:
        sen.sendto(Message, (IP, port))
        i+=1
