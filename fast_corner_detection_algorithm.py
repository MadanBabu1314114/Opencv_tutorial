import cv2 as cv
import numpy as np


img = cv.imread("image3.jpg")

img = cv.resize(img, fx=2, fy=2, dsize=None, interpolation=cv.INTER_CUBIC)

gray_img = cv.cvtColor(src=img, code=cv.COLOR_BGRA2GRAY)

fast = cv.FastFeatureDetector_create()
kp = fast.detect(img, None)
keypoint = cv.drawKeypoints(image=gray_img, keypoints=kp,
                            outImage=img, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

while (1):
    cv.imshow("Original Image", img)
    cv.imshow("Fast image", gray_img)
    if cv.waitKey(1) & 0xFF == ord('s'):
        break
cv.destroyAllWindows()
