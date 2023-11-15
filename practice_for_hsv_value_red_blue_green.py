import cv2 as cv
import numpy as np
import sys

cap =cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    
    #Red colors
    lower_red =   np.array([0, 100 , 100])    
    upper_red =   np.array([10 , 255  , 255]) 
    
    
    #Blue colors
    lower_blue =    np.array([110 , 100 , 100])
    upper_blue =       np.array([130 , 255 , 255])
    
    
    #green Colors
    lower_green = np.array([50 , 100, 100])
    upper_green = np.array([70  , 255 , 255])
    
    #createing the hsv frame 
    hsv = cv.cvtColor(frame , cv.COLOR_BGR2HSV)
    
    mask_for_red = cv.inRange(hsv , lower_red,   upper_red , )
    mask_for_green = cv.inRange(hsv ,   lower_green  , upper_green)
    mask_for_blue = cv.inRange(hsv  ,  lower_blue ,  upper_blue)
    
    res_for_red = cv.bitwise_and(frame , frame ,mask = mask_for_red)
    res_for_blue = cv.bitwise_and(frame , frame  , mask =mask_for_blue)
    res_for_green = cv.bitwise_and(frame , frame  , mask=mask_for_green)
    
    cv.imshow("res_for_green"  , res_for_green )
    cv.imshow("res_for_red"  , res_for_red )
    cv.imshow("res_for_blue" , res_for_blue)
    cv.imshow("my video" , frame)
     
    if cv.waitKey(1) ==ord('s'):
        break


cap.release()
cv.destroyAllWindows()