import  cv2 as cv
import sys
import numpy as np

img = np.zeros((512,512 , 3) , np.uint8)

cv.line(img , (0,0) , (312 , 312) , (255 , 0 , 0) , 5)

font =  cv.FONT_HERSHEY_COMPLEX
cv.putText(img , "Hello madan" , (250 , 200) , font, 1 , (255 , 164 , 200) , 2 , 3)

while True:
    cv.imshow("image", img)
    if cv.waitKey(0) == ord('s'):
        break
