import time
import cv2 as cv
import numpy as np
import sys


img1 = cv.imread("image.jpg")
img2 = cv.imread("m.jpg")

img2 = cv.resize(img2 , (img1.shape[1] , img1.shape[0]))

start = 1
end = 100
 
cv.namedWindow("Image_blending")
while (1):
    dst =cv.addWeighted(img1 , start/100 , img2 ,end/100 - start/100 , 0 )
     
    cv.imshow("Image_blending" ,dst )
    time.sleep(1)  # import time
    start = start + 5
    if  start >= 100:
        break
    if cv.waitKey(1) & 0xFF == ord('s'):
        break 
    
cv.destroyAllWindows()
    