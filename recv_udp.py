import socket
import sys
import cv2
import numpy as np
'''
This is the prototype for the UDP reciever
'''

HOST=''
PORT=5000

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((HOST,PORT))
print ('Socket created')

t=b''
while True:
    data, addr = s.recvfrom(90000)
    frame = np.fromstring (data, dtype=np.uint8)
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break