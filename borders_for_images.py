import cv2 as cv
import numpy as np
import sys
import matplotlib.pyplot as plt
 
img  = cv.imread("a1qo2eh_ms-dhoni-afp_625x300_15_June_20.jpg")
cv.namedWindow("Image")
img = cv.copyMakeBorder(img , top=10 , bottom=10 , left=10 , right=10 , borderType=cv.BORDER_CONSTANT , value=[255, 143 , 145])
# while (1):
#     cv.imshow("Image" , img)    
#     if cv.waitKey(1) & 0xFF == ord('s'):
#         break

plt.subplot(231), plt.imshow(img , 'gray') ,plt.title("Border Constant") 
plt.show()


        

