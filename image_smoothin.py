import cv2 as cv
import numpy as np
import sys

img = cv.imread("a1qo2eh_ms-dhoni-afp_625x300_15_June_20.jpg")
#Method 1 Averaging
smooth_img = cv.blur(img , (5,5))

#Method 2 Gaussion Bluring
gaussion_blur_img = cv.GaussianBlur(src=img , ksize=(5,5),sigmaX=0 , sigmaY=0 )

#Method 3 Median Bluring
median_blur = cv.medianBlur(src=img , ksize=5)

#Method 4 Bilateral Filtering
bilateral_img = cv.bilateralFilter(src=img  , d= 9 , sigmaColor=75 , sigmaSpace=75)
while (1) :
    cv.imshow("Averaging Image" , smooth_img)
    cv.imshow("Median Blur " , median_blur)
    cv.imshow("Gaussion Blur Image" , gaussion_blur_img)
    cv.imshow("Bilateral Filtering" , bilateral_img)
    cv.imshow("Image" , img)
    if cv.waitKey(1) == ord('s'):
        break
    
cv.destroyAllWindows()