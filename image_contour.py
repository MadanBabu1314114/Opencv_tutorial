import cv2 as cv
import numpy as np
import sys

img = cv.imread("image3.jpg")
img = cv.resize(img , fx = 2 , fy = 2  , interpolation=cv.INTER_CUBIC , dsize=None)
img = cv.cvtColor(src=img ,code = cv.COLOR_BGRA2GRAY)
contours , hierarchy = cv.findContours(image=img , mode=cv.RETR_TREE , method=cv.CHAIN_APPROX_SIMPLE,)
cv.drawContours(image=img , contours=contours , contourIdx=-1 , color=(154 , 142 , 178) , thickness=20)
while (1):
    cv.imshow("Image" , img)
    if cv.waitKey(1) & 0xFF == ord(('s')):
        break
    
cv.destroyAllWindows()
