import socket
import sys
import cv2
import _pickle
import numpy as np
import struct 
def tcp_open(host, port):
    HOST=host
    PORT=port
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print ('Socket created')
    s.bind((HOST,PORT))
    print ('Socket bind complete')
    s.listen(10)
    print ('Socket now listening')
    conn = s.accept()[0]
    return conn

HOST=''
PORT=8089

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print ('Socket created')

s.bind((HOST,PORT))
print ('Socket bind complete')
s.listen(10)
print ('Socket now listening')

conn,addr=s.accept()


data = b''
payload_size = struct.calcsize("L") 
while True:
    data = conn.recv(90000)
    frame = np.fromstring (data, dtype=np.uint8)
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    if type(frame) is np.ndarray:
        cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break