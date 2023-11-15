import cv2 as cv
import sys 
import numpy  as np

img = np.ones((1000 , 1000 , 3) ,np.uint8 )

def nothing(x):
    pass
cv.namedWindow("Video")
cv.createTrackbar("R" , "Video" ,  0  ,  255 , nothing)
cv.createTrackbar("G" , "Video" ,  0  ,  255 , nothing)
cv.createTrackbar("B" , "Video" ,  0  ,  255 , nothing)
switch = "0 is off \n 1 is on"

cv.createTrackbar(switch , "Video" , 0 , 1 , nothing)


while (1):
     
    cv.imshow(winname="Video" , mat=img)
    if  cv.waitKey(1) & 0xFF == ord('s'):
        break
    
    r = cv.getTrackbarPos(trackbarname="R" , winname="Video")
    g = cv.getTrackbarPos(trackbarname="G" , winname="Video")
    b = cv.getTrackbarPos(trackbarname="B" , winname="Video")
    s = cv.getTrackbarPos(trackbarname= switch , winname="Video")
    
    img[:] = [b, g , r]
        
cv.destroyAllWindows()