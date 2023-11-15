import  cv2 as cv

img1 = cv.imread("m.jpg")
img2 = cv.imread("image.jpg")

#img = a.alph + b.beta + gamma
 
img2= cv.resize(img2 , (img1.shape[1] , img1.shape[0]))
print(img1.size)
print(img2.size)
  
img = cv.addWeighted(img1 , 0.5 , img2 , 0.5 , 0)

cv.namedWindow("dst")
 
while True: 
    cv.imshow("dst" ,img )
    if cv.waitKey(1) == ord('s'):
        break
cv.destroyAllWindows()