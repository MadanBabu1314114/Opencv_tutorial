import cv2 as cv
import numpy as np
import sys


def nothing(x):
    print(x)
    pass

 
def drawCircles(event ,x , y , flags , parms):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img , (x , y) , radius_of_cricle , thickness=5 , color=(255 , 165 , 178))
    pass

 
img  = np.ones((600 , 600 , 3) , np.uint8) *255
cv.namedWindow('Video')
cv.setMouseCallback('Video' , drawCircles)
radius_of_cricle = cv.createTrackbar("Radius" , "Video" , 0 , 200 , nothing)
while (1):
    cv.imshow("Video" , img)
    radius_of_cricle = cv.getTrackbarPos('Radius' , "Video")
    if cv.waitKey(1) & 0xFF == ord('s'):
        break

cv.destroyAllWindows()