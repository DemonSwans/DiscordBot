import cv2
import time
import numpy as np
cap = cv2.VideoCapture(0)
static_gray = None
static_bgr = None
for _ in range(10):
    time.sleep(1)
while(True):
    ret, frame = cap.read()
    grayf = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if static_gray is None:
        static_gray = grayf
    diff_frame = cv2.absdiff(static_gray, grayf)
    thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    cnts, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    motion = None
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        motion = 1
        with open("ruch.txt", "w") as czyruch:
            print("1")
            czyruch.write("1")
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    time.sleep(0.5)
    if motion == 1:
        with open("ruch.txt", "w") as czyruch:
            czyruch.write("0")
        motion = 0


    cv2.imshow('RGB', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()