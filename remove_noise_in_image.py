import cv2 as cv
import numpy as np
import sys

cap = cv.VideoCapture(0)

while (1):
	_ , frame = cap.read()

	if not _:
		print("Not create the frame")
		pass
	dst =  cv.fastNlMeansDenoisingColored(frame,None,10,10,7,21)
	cv.imshow('Video' , frame)
	cv.imshow("NOiseless video" , dst)
	if cv.waitKey(1) & 0xFF  ==ord('s'):
		break
cv.destroyAllWindows()