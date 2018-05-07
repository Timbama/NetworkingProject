import numpy
import math
import cv2
def psnr(img1, img2):
    mse = numpy.mean( (img1 - img2) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

orig = cv2.VideoCapture('G:/timba/Documents/Network Project/NetworkingProjectTextInMotion-Sample-720p.mp4')
after = cv2.VideoCapture('G:/timba/Documents/Network Project/outpy.avi')
frames = orig.get(cv2.CAP_PROP_FRAME_COUNT)
print(frames)
frames = after.get(cv2.CAP_PROP_FRAME_COUNT)
print(frames)
img1 = orig.read()[1]
