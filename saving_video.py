import  cv2 as cv
import  sys

print(cv.__version__)
cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter("output.avi" , fourcc , 100, (680 , 400) )
if not cap.isOpened():
    print("Video Capturing is not working ")
    exit(0)

while cap.isOpened():
    ret , frame = cap.read()

    if not ret :
        print("Not returm any thing to the camera")
        exit(0)

    out.write(frame)
    cv.imshow("video of the madan" , frame)
    if cv.waitKey(0) == ord('s'):
        break

cap.release()
cv.destroyAllWindows()