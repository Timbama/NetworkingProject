import socket
import cv2
import numpy as np
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
IP= "192.168.2.8"
port = 5000
Message="test".encode()
cap = cv2.VideoCapture(1)
sen=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
        ret, frame = cap.read()
        result, encimg = cv2.imencode('.jpg', frame)
        print(encimg.shape)
        d = encimg.flatten()
        s = d.tostring()
        sen.sendto(Message, (IP, port))
