import cv2 as cv
import sys
import numpy as np

img = cv.imread(filename="image3.jpg" , flags=cv.IMREAD_GRAYSCALE)
edge_img = cv.Canny(image=img , threshold1=22 , threshold2=255 ,apertureSize=3 )
lines = cv.HoughLinesP(edge_img, 1, np.pi/80, 1100,
                       minLineLength=100, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(edge_img, (x1, y1), (x2, y2), (255 , 145,135), 2)
while True:
    cv.imshow("original image" , img)
    cv.imshow("Edge image" , edge_img)    
    if cv.waitKey(1) == ord('s'):
        break

cv.destroyAllWindows()
