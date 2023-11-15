import cv2 as cv
import sys
import numpy as np

img = cv.imread("a1qo2eh_ms-dhoni-afp_625x300_15_June_20.jpg")


def find_the_postion_of_bat(event , x , y , flags , parms):
    if event == cv.EVENT_LBUTTONDBLCLK:
        print("X = " , x)
        print("Y = " , y)
        font  = cv.FONT_HERSHEY_SIMPLEX
         
        cv.putText(img=img , text = str(x)+"  "+str(y), org=(x , y) , fontFace=font , color=(255 , 255, 255) , thickness=2  , fontScale=1)

cv.namedWindow("Video")
cv.setMouseCallback("Video" ,find_the_postion_of_bat )

 

while (1):
    cv.imshow("Video" , img)
    if cv.waitKey(1) & 0xFF == ord("s"):
        break

print("Shape of the image " , img.shape)
print('Datatypw of the image '  , img.dtype)
print("Size of the image " , img.size)
print("ITem size of the image " , img.itemsize)

cv.destroyAllWindows()