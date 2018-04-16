import cv2
import numpy as np
import socket
import sys
import _pickle
import struct 
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

cap=cv2.VideoCapture(1)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('10.100.68.207',8089))

while True:
    ret,frame=cap.read()
    img_str = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 90])[1].tostring()
    print(len(img_str))
    clientsocket.sendall(img_str)