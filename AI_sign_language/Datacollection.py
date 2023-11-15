import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math

import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

offset = 20
imgSize = 300

folder = "data/Hello"
counter = 0
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox']

        imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255
        imgCrop = img[y-offset : y+ h+offset,x-offset : x+w+offset]
        imgCropShape = imgCrop.shape
        Ratio  = h/w
        if Ratio >1:
            k = imgSize/h
            wCal  = math.ceil(k*w) 
            imgResize = cv2.resize(imgCrop,(wCal, imgSize))
            imgResizeShape = imgResize.shape
            Wgap = math.ceil((imgSize-wCal)/2)
            imgWhite[:,Wgap:wCal+Wgap] = imgResize
        else:
            k = imgSize/w
            hCal  = math.ceil(k*h)
            imgResize = cv2.resize(imgCrop,(imgSize, hCal))
            imgResizeShape = imgResize.shape
            hgap = math.ceil((imgSize-hCal)/2)
            imgWhite[hgap:hCal+hgap,:] = imgResize
        #cv2.imshow('ImageCrop', imgCrop)
        cv2.imshow('ImageWhite',imgWhite)
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('s'):
        counter += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.png',imgWhite)
        print(counter)