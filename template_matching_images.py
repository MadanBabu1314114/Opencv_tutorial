import cv2 as cv
import numpy as np

img = cv.imread("a1qo2eh_ms-dhoni-afp_625x300_15_June_20.jpg"  ,flags=cv.IMREAD_GRAYSCALE)
W , H = img.shape[:2]
img2 = img.copy()
template = cv.imread("short_dhoni.jpg" , flags=cv.IMREAD_GRAYSCALE)
w , h = template.shape[::-1]
res = cv.matchTemplate(image=img2 , templ=template , method=cv.TM_CCOEFF )
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
top_left = min_loc  
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
print(bottom_right)
cv.rectangle(img=img2 , pt1=top_left , pt2=bottom_right , color=(255 , 145 , 167) ,)
while True:
    cv.imshow("template" , template)
    cv.imshow("original image" , img)
    cv.imshow("match_template" , img2)    
    if cv.waitKey(1) == ord('s'):
        break

cv.destroyAllWindows()