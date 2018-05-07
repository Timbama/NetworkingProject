import socket
import cv2
import numpy as np
def send_udp(frame, host, port, sock):
        '''
        This function send compressed data over UDP
        '''
        img_str = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 90])[1].tostring()
        print(len(img_str))
        sock.sendto(img_str, (host, port))
'''
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
IP= "10.100.68.207"
port = 5000
Message="test".encode()
cap = cv2.VideoCapture(1)
sen=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
        ret, frame = cap.read()
        img_str = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 90])[1].tostring()
        print(len(img_str))
        sen.sendto(img_str, (IP, port))
'''
