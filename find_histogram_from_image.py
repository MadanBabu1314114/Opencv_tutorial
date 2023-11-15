import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread("a1qo2eh_ms-dhoni-afp_625x300_15_June_20.jpg",flags=cv.IMREAD_GRAYSCALE)

histogram_img = cv.calcHist(images=[img] , channels=[0] , mask=None ,histSize=[256] ,ranges=[0 , 526])
histogram_img = cv.resize(src=histogram_img , fx = 2 ,fy = 2 , interpolation= cv.INTER_CUBIC , dsize=None)

hist , bins = np.histogram(img.ravel() , 256 , [0,256])
print(hist)
plt.hist(img.ravel() , 256 , [0,256]) , plt.show()
while (1):
    cv.imshow("Image", img)
    cv.imshow("HIst_image" , histogram_img)
    if cv.waitKey(1) & 0xFF == ord('s'):
        break
cv.destroyAllWindows()
