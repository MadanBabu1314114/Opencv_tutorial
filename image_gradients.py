import cv2 as cv
import numpy as np
import sys

img = cv.imread("image3.jpg")

img = cv.resize(img , fx=2 , fy = 2 , interpolation=cv.INTER_CUBIC , dsize=None)

img = cv.cvtColor(src=img , code=cv.COLOR_BGR2GRAY)
sobel_x = cv.Sobel(src=img , ksize=1 , dx= 1, dy = 0 ,ddepth=cv.CV_64F )
sobel_y = cv.Sobel(src=img , ksize=1 , dx= 0, dy = 1 ,ddepth=cv.CV_64F )
lap = cv.Laplacian(src=img , ddepth=cv.CV_64F , ksize=1)

while (1) :    
    cv.imshow("Image" , img)
    cv.imshow("sobel X" , sobel_x)
    cv.imshow("sobel Y" , sobel_y)
    cv.imshow("Laplacian image" ,lap )
    if cv.waitKey(1) & 0xFF == ord('s'):
        break

cv.destroyAllWindows()