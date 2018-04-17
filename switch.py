import socket
import numpy as np
import cv2
import threading
import time
from send_tcp import open_tcp, send_tcp 
from send_udp import send_udp
cap = cv2.VideoCapture(1)
encode_param = [cv2.IMWRITE_JPEG_QUALITY, 90]
host = '10.0.1.36'
port = 8089
t_end = 60 * .5
motion  = False
conn_open = False

sen = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
    if motion:
        while time.time () < time.time() + t_end:
            frame = cap.read()[1]
            if not(conn_open):
                sen.sendto('TCP', (host, port))
                time.sleep(3)
                sock = open_tcp(host, port)
                conn_open = True
            else:
                send_tcp(frame, sock)
    else:
        frame = cap.read()[1]   
        if conn_open:
            sock.sendall('UDP')
            send_udp(frame, host, port, sen)
        else:
            send_udp(frame, host, port, sen)
