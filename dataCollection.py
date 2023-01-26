import math
import time

import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
capture = cv2.VideoCapture(0)
detect = HandDetector(maxHands=1)
space = 30
size=400
c=0
while True:
    result, img = capture.read()
    hands, img = detect.findHands(img)
    white = np.ones((size,size,3),np.uint8)*255
    if hands:
        x, y, w, h = hands[0]['bbox']
        crop = img[y-space:y+h+space, x-space:x+w+space]

        if(h>=w):
            times=size/h
            new_width=math.ceil(w*times)
            newsize=cv2.resize(crop,(new_width,size))
            left_gap=math.ceil((size-new_width)/2)
            white[:, left_gap:left_gap+newsize.shape[1]] = newsize
        else:
            times = size / w
            new_height = math.ceil(h * times)
            newsize = cv2.resize(crop, (size,new_height))
            top_gap = math.ceil((size - new_height) / 2)
            white[top_gap:top_gap + new_height, :] = newsize

        cv2.imshow("crop", crop)
        cv2.imshow("white", white)

    # cv2.imshow("White screen",white)
    cv2.imshow("image", img)
    press=cv2.waitKey(1)
    if press==ord("a"):
        c=c+1
        cv2.imwrite(f'Data/J/handImage_{time.time()}.jpg',white)
        print(c)



