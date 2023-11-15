import numpy as np
import cv2 as cv


green  = np.uint8([[[0 , 255 , 0]]])
hsv_value_for_green = cv.cvtColor(green , cv.COLOR_BGR2HSV)
print("HSV value for green = " , hsv_value_for_green  )

blue  = np.uint8([[[255 , 0 , 0]]])
hsv_value_for_blue = cv.cvtColor(blue , cv.COLOR_BGR2HSV)
print("HSV value for blue = " , hsv_value_for_blue  )


red  = np.uint8([[[0 , 0 , 255]]])
hsv_value_for_red = cv.cvtColor(red , cv.COLOR_BGR2HSV)
print("HSV value for red = " , hsv_value_for_red )
