import cv2 as cv
import numpy as np
import sys

img = cv.imread("image2.jpg")
img_dhoni = cv.imread("a1qo2eh_ms-dhoni-afp_625x300_15_June_20.jpg")


kernel = np.ones((5,5) , np.uint8)
#Erosion method 

erosion_img = cv.erode(src=img , kernel=kernel , iterations=1)

#Dilation method
dilation_ing = cv.dilate(src=img , kernel=kernel , iterations=1)

#Opening method
opening_img = cv.morphologyEx(src=img , kernel=kernel , iterations=1 , op=cv.MORPH_OPEN)

#closing method 
closing_img = cv.morphologyEx(src=img , kernel=kernel , iterations=1 , op=cv.MORPH_CLOSE)

#Gradient mehod
gradient_img = cv.morphologyEx(src=img , kernel=kernel , iterations=1 , op=cv.MORPH_GRADIENT ,) 


#Top hat method
top_hat_img = cv.morphologyEx(src=img , kernel=kernel , iterations=1 , op=cv.MORPH_TOPHAT ,)

#Black Hat
black_hat_img = cv.morphologyEx(src=img , kernel=kernel , iterations=1 , op=cv.MORPH_BLACKHAT ,)

while (1) :
    cv.imshow("Image" , img)
    cv.imshow("Erosion Image" , erosion_img , )
    cv.imshow("Dilation image" , dilation_ing)
    cv.imshow("Opening Image" ,opening_img)
    cv.imshow("Closing image" ,closing_img)
    cv.imshow("Gradient Image" , gradient_img)
    cv.imshow("Top hat image" , top_hat_img)
    cv.imshow("Black Hat image" , black_hat_img)
    if cv.waitKey(1) & 0xFF == ord('s'):
        break


cv.destroyAllWindows()