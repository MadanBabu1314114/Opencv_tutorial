import cv2 as cv
import numpy as np

img = cv.imread('star.jpg')
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(image=gray  , maxCorners=25 , qualityLevel=0.04 , minDistance=10 ,)
 
corners = np.int0(corners)
for i in corners:
    x, y = i.ravel()
    cv.circle(gray, (x, y), 3, (134 , 154 ,134), -1)

while (1):
    cv.imshow("Original Image" , img)
    cv.imshow("shi and tomais" , gray)
    if cv.waitKey(1) & 0xFF == ord('s'):
        break
cv.destroyAllWindows()
