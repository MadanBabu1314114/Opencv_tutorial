import  cv2 as cv
import sys

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Capture video is not opened")
    exit(0)

while True:
    ret , frame = cap.read()
    if not ret :
        print("not captured the frame")
        exit(0)
    # cv.imshow("Hello Madan" , frame)
    gray_color_imag = cv.cvtColor(frame , cv.COLOR_BGR2GRAY)

    cv.imshow("Gray colored image" , gray_color_imag)

    if cv.waitKey(1 ) == ord('s'):
        break

cap.release()
cv.destroyAllWindows()
