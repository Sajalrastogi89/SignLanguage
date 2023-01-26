import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
capture = cv2.VideoCapture(0)
detect = HandDetector(maxHands=1)
space = 30
size=400
while True:
    result, img = capture.read()
    hands, img = detect.findHands(img)
    white = np.ones((size,size,3),np.uint8)*255
    if hands:
        x, y, w, h = hands[0]['bbox']
        crop = img[y-space:y+h+space, x-space:x+w+space]
        white[0:crop.shape[0], 0:crop.shape[1]] = crop
        if(h>w):
            times=size/h
            new_width=w*times
            resize=cv2.resize()




        cv2.imshow("crop", crop)
        cv2.imshow("white", white)

    # cv2.imshow("White screen",white)


    cv2.imshow("image", img)
    cv2.waitKey(1)

