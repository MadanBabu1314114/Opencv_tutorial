import cv2 as cv
import sys
import numpy as np

img = np.ones((1000 , 1000 , 3) , np.uint8) *200 

def drawCircle(event  , x , y  , flags , parms):
    
    if event == cv.EVENT_LBUTTONDBLCLK:
        print("Madan")
        cv.circle(img=img , thickness=1, center=(x, y), radius=100 , color=(154 , 255 , 154)  )
    if event == cv.EVENT_MOUSEMOVE:
        print("Babu")
        cv.rectangle(img=img , color=(156 , 255  , 134) , pt1=(x , x - 150) , pt2=(y - 150 , y) , thickness=2 , )
         
    pass
cv.namedWindow("Video")
cv.setMouseCallback("Video" , drawCircle)
while (1):
    cv.imshow("Video" , img )
    if cv.waitKey(20) == ord('s'):
        break
cv.destroyAllWindows()