import cv2
import numpy as np
import socket
import sys
import _pickle
import struct 

cap=cv2.VideoCapture(1)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('10.0.1.36',8089))

while True:
    ret,frame=cap.read()
    data = _pickle.dumps(frame, protocol=2 )
    clientsocket.sendall(struct.pack("L", len(data))+data)