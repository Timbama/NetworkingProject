#Server prog

import socket
import numpy
import time
import cv2

UDP_IP="127.0.0.1"
UDP_PORT = 999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

s=""

while True:
      data, addr = sock.recvfrom(259200)
      s+= data
      if len(s) == (259200*20):
          frame = numpy.fromstring (s, dtype=numpy.uint8)
          frame = frame.reshape(720,1280,3)
          cv2.imshow("frame",frame)

          s=""
      if cv2.waitKey(1) & 0xFF == ord('q'):
          break