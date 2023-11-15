import cv2 as cv
import numpy as np
import sys


start_point = (-1, -1)
end_point = (-1, -1)
i = 0
j = 0
k = 0
l = 0
rect = 0


def onMouse(event, x, y, flags, params):
    global start_point
    global end_point
    if event == cv.EVENT_LBUTTONDOWN:
        start_point = (x, y)
    elif event == cv.EVENT_LBUTTONUP:
        end_point = (x, y)
        cv.rectangle(img, start_point, end_point,
                     color=(255, 134, 167), thickness=5)
        print(list(start_point + end_point))


img = cv.imread("a1qo2eh_ms-dhoni-afp_625x300_15_June_20.jpg")
img2 = img .copy()
w,h = img.shape[:2]
mask = np.zeros(img.shape[:2], np.uint8)
bgdmodel = np.zeros((1 , 65), np.float64)
fgdmodel = np.zeros((1 , 65), np.float64)
# grad_cut_image = cv.grabCut(img=img , mask=None ,  , bgdModel=bgdmodel , fgdModel=fgdmodel , iterCount=5 , mode= cv.GC_INIT_WITH_RECT)

# cv.namedWindow("Original Image")
# cv.setMouseCallback("Original Image", onMouse)


while (1):

    # if cv.waitKey(1) == ord('n'):
    print("Madan")
    cv.grabCut(img=img, mask=mask, rect=(89, 73, 503, 567), bgdModel=bgdmodel, fgdModel=fgdmodel, iterCount=5, mode=cv.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # Multiply the image with the binary mask to get the segmented image
    result = img * mask2[:, :, np.newaxis]
    cv.imshow(winname="Original Image", mat=result)
    cv.imshow(winname=" Image", mat=img2)
    if cv.waitKey(1) & 0xFF == ord('s'):
        break
cv.destroyAllWindows()
