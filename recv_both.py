import socket
import sys
import cv2
import _pickle
import numpy as np
import struct 
from recv_tcp import tcp_open
# setup a host and port number
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 25,(1280,720))
host = '10.0.1.22'
port = 8089
# create a UDP scocket to recieve data and bind it to the port
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',port))

print ('Socket created')
# recieve the initial state of the system
data, addr = s.recvfrom(90000)
while True:  
    # if the state of the system is TCp then setup the TCP connection
    if data == b'TCP':
        conn = tcp_open(host, port)
        while True:
            # run in a loop until the switch command is received
            data = conn.recv(90000)
            if data == b'UDP':
                break
            else:
                # decode the frame from a string to a jpg then to a numpy array
                frame = np.fromstring (data, dtype=np.uint8)
                frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
                if type(frame) is np.ndarray:
                    cv2.imshow('frame',frame)
                    out.write(frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    else:
        # if the UDP option is selected then loop through reccieving over UDP
        while True:
            data, addr = s.recvfrom(90000)
            # break if the TCP command is sent
            if data == b'TCP':
                break
            else:
                frame = np.fromstring (data, dtype=np.uint8)
                frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
                cv2.imshow('frame',frame)
                out.write(frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    out.release()
                    break


