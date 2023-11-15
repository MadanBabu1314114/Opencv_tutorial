import cv2 as cv
import numpy as np
import sys

img = cv.imread("a1qo2eh_ms-dhoni-afp_625x300_15_June_20.jpg")

py_img_down = img.copy()

list_of_pyramid_down = [img]
for i in range(1,4):
    py_img_down = cv.pyrDown(src=py_img_down)
    list_of_pyramid_down.append(py_img_down)




count = 0
while (1):

    if count == 0:
        for i in list_of_pyramid_down:
            cv.imshow( "Image"+str(i), i)
            count = count + 1
    if cv.waitKey(1) & 0xFF == ord(('s')):
        break
    
cv.destroyAllWindows()
