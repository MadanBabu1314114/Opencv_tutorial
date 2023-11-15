import cv2 as cv

img = cv.imread("star.jpg" , flags=cv.IMREAD_GRAYSCALE)

_ , thresh = cv.threshold(src= img , thresh=122 , maxval= 255 , type=cv.THRESH_BINARY)

#finding the contours
contour  , hierarichy = cv.findContours(image=img , mode=1 ,method=2)

#selectsing one  contour
cnt = contour[0]

#finding he moments for contour
M = cv.moments(cnt)

#finding the center of trhe mass of the object
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

#finding the area of contour
area = cv.contourArea(cnt)
print(area)


#finding the perimeter of the contour
perimeter = cv.arcLength(cnt , closed=True)
print(perimeter)

#finding is it convex curve or not
c = cv.isContourConvex(cnt)
print(c)

#drw the rectangle on the  contour
x ,y , h  , w = cv.boundingRect(cnt)
cv.rectangle(img=img , pt1=(x ,y) , pt2=(x+h , y+w) , color=(255 , 0 , 0) , thickness=10)
# cv.circle(img=img , center=(cx , cy) , radius=4 , color=(255,  0 , 0) ,thickness=3  )
 
while (1):
    cv.imshow("Image" , img)
    if cv.waitKey(1) & 0xFF == ord('s'):
        break
cv.destroyAllWindows()     


