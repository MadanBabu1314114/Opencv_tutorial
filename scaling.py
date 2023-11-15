import cv2 as cv
import sys

img = cv.imread("m.jpg")
cv.namedWindow("Image")

img2 = cv.resize(img , fx = 2 , fy = 2 ,interpolation=cv.INTER_CUBIC , dsize=None)
while True:
    cv.imshow("Image" , img2)
    if cv.waitKey(1) == ord('s'):
        break

cv.destroyAllWindows()