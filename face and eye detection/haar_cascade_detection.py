import cv2 as cv
import numpy as np
import sys
import argparse

def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h,x:x+w]
        #-- In each face, detect eyes
        eyes = eye_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
    cv.imshow('Capture - Face detection', frame)



parser = argparse.ArgumentParser(description="Here the face and eye detection ")
parser.add_argument("--face_cascade" , help='path of the face detection model'  , default="haarcascade_frontalface_alt.xml")
parser.add_argument("--eye_cascade" , help='path of the eye detection model'  , default="haarcascade_eye.xml")
args = parser.parse_args()

cap = cv.VideoCapture(0)

face_cascade_name = args.face_cascade
eye_cascade_name = args.eye_cascade

face_cascade = cv.CascadeClassifier(face_cascade_name)
eye_cascade = cv.CascadeClassifier(eye_cascade_name)

while (1):
    _ , frame = cap.read()
    
    cv.imshow("Original Video" , frame)
    detectAndDisplay(frame)
    if cv.waitKey(1) & 0xFF == ord('s'):
        break

cv.destroyAllWindows()