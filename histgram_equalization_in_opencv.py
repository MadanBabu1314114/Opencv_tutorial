import cv2 as cv

img = cv.imread("image2.jpg",
                cv.IMREAD_GRAYSCALE)
equlibrium_img = cv.equalizeHist(src=img)

clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(4,4))
clahe_img = clahe.apply(img)
while True:
    cv.imshow("Image", img)
    cv.imshow("qu_Image", equlibrium_img)
    cv.imshow("clahe img", clahe_img)
    if cv.waitKey(1) == ord('s'):
        break

cv.destroyAllWindows()
