import cv2 as cv
import numpy as np
import sys

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("not Open Camera")
    sys.exit(0)
 
while True:
    _ , frame  = cap.read()
    hsv = cv.cvtColor(frame , cv.COLOR_BGR2HSV)
    #here installizing the two colors 
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    mask = cv.inRange(hsv , lower_blue , upper_blue)
    
    res = cv.bitwise_and(frame ,frame , mask=mask)
    
    cv.imshow("hsv"  , hsv)
    cv.imshow('mask' , mask)
    cv.imshow("Frame" , frame)
    cv.imshow("res" , res)
    
    
    if cv.waitKey(1) ==ord("s"):
        break
cap.release()
cv.destroyAllWindows()