import cv2 as cv
import numpy as np

img = cv.imread("m.jpg")
# img = cv.resize(img , dsize=None , fx=2 , fy=2 , interpolation=cv.INTER_CUBIC)
rows , columns , matrix = img.shape
M =  cv.getRotationMatrix2D(((columns-1)/2.0,(rows-1)/2.0),90,1)
while True:
    dst = cv.warpPerspective(img ,M=M , dsize=(columns , rows) )
    cv.imshow("Image" , img)
    cv.imshow("transltion Image" , dst)
    if cv.waitKey(1) == ord('s'):
        break

cv.destroyAllWindows()