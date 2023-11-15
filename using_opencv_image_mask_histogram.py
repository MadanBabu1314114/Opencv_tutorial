import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image2.jpg", cv.IMREAD_GRAYSCALE)
mask = np.zeros(img.shape[:2], np.uint8)

mask[100:300, 100:400] = 255
masked_img = cv.bitwise_and(img, img, mask=mask)
hist_img_without_mask = cv.calcHist(
    images=[img], channels=[0], mask=None, ranges=[0, 256] , histSize=[256])
hist_img_with_mask = cv.calcHist(
    images=[img], channels=[0], mask=mask, ranges=[0, 256] , histSize=[256])

plt.subplot(231), plt.imshow(img, "gray")
 
plt.subplot(233), plt.imshow(masked_img, 'gray')
plt.subplot(234),  plt.plot(hist_img_with_mask ,) , plt.plot(hist_img_without_mask) ,plt.legend(['hist_img_with_mask' , 'hist_img_without_mask'])
plt.xlim([0,256])
 
plt.show()

print(img.shape[:2])
