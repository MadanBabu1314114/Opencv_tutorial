import cv2 as cv

img1 = cv.imread("a1qo2eh_ms-dhoni-afp_625x300_15_June_20.jpg")
img2 = cv.imread("short_dhoni.jpg")

orb = cv.ORB_create()

kp1, dec1 = orb.detectAndCompute(img1, None)
kp2, dec2 = orb.detectAndCompute(img2, None)

bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

matches = bf.match(dec1 , dec2)

# Sort them in the order of their distance.
matches = sorted(matches, key=lambda x: x.distance)

# Draw first 10 matches.
img3 = cv.drawMatches(img1, kp1, img2, kp2,
                      matches, None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)


while (1):
    cv.imshow("Image1", img1)
    cv.imshow("Image2", img2)
    cv.imshow("BF Matcher " , img3)
    if cv.waitKey(1) & 0xFF == ord('s'):
        break
cv.destroyAllWindows()
