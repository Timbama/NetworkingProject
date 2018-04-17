import socket
import sys
import cv2
import _pickle
import numpy as np
import struct 
from recv_tcp import tcp_open

host = ''
port = 8089

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
print ('Socket created')
conn = tcp_open(host, port)
data, addr = s.recvfrom(1024)
while True:  
    if data.decode() == 'TCP':
        while True:
            if data.decode() == 'UDP':
                break
            else:
                data = conn.recv(90000)
                frame = np.fromstring (data, dtype=np.uint8)
                frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
                if type(frame) is np.ndarray:
                    cv2.imshow('frame',frame)
    else:
        while True:
            if data.decode() == 'TCP':
                break
            else:
                data, addr = s.recvfrom(90000)
                frame = np.fromstring (data, dtype=np.uint8)
                frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
                cv2.imshow("frame",frame)


