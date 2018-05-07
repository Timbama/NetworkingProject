import cv2
import numpy as np
import socket
import sys
import _pickle
import struct 
cap=cv2.VideoCapture(1)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
def open_tcp(host, port):
    '''
    this opens the send side TCP connection 
    '''
    clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientsocket.connect((host,port))
    return clientsocket
def send_tcp(frame, sock):
    '''
    This function compresses and send data over TCP
    '''
    img_str = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 90])[1].tostring()
    print(len(img_str))
    sock.sendall(img_str)

'''
sock = open_tcp('10.100.68.207', 8089)


while True:
    ret,frame=cap.read()
    send_tcp(frame,sock)
'''