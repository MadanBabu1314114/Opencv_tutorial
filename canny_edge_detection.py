import cv2 as cv
import numpy as np

img  =cv.imread("a1qo2eh_ms-dhoni-afp_625x300_15_June_20.jpg")

canny_img= cv.Canny(image=img , threshold1=122 , threshold2=255)
while (1) :    
    cv.imshow("Image" , img)
    cv.imshow("Canny Image", canny_img)
    if cv.waitKey(1) & 0xFF == ord('s'):
        break

cv.destroyAllWindows()