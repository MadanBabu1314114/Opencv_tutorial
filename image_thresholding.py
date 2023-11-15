import cv2 as cv
import numpy as np
import sys

img  = cv.imread("a1qo2eh_ms-dhoni-afp_625x300_15_June_20.jpg")
gray_color_img =  cv.cvtColor(img , cv.COLOR_BGR2GRAY)
ret,thresholding_img = cv.threshold(src=gray_color_img ,thresh=122 , maxval=255 , type=cv.THRESH_BINARY)
adepative_thresholding_img = cv.adaptiveThreshold(src=gray_color_img , maxValue=255  , adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C , thresholdType=cv.THRESH_BINARY , blockSize=11 , C = 2)
while True:
    cv.imshow("Image" , img)
    cv.imshow("Thresholding image" , thresholding_img)
    cv.imshow("Adaptive Thresholding Image" , adepative_thresholding_img)
    if cv.waitKey(1) == ord('s'):
        break

cv.destroyAllWindows()