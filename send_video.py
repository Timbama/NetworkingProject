import socket
import numpy as np
import cv2
UDP_IP = '10.0.1.36'                  
<<<<<<< HEAD
UDP_PORT = 4096        
cap = cv2.VideoCapture(0)
=======
UDP_PORT = 999        
cap = cv2.VideoCapture('drop.avi')
>>>>>>> 9ea5d95fd2885ee492bb99b92021823c21b44fc3
while(True):
   ret, frame = cap.read()
   cv2.imshow('frame',frame)
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   d = frame.flatten() 
   s = d.tostring ()
   print(len(s))
   for i in range(20):
        sock.sendto (s[i*46080:(i+1)*46080],(UDP_IP, UDP_PORT))

        if cv2.waitKey(1) & 0xFF == ord('q'):
          break

cap.release()
cv2.destroyAllWindows()