import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

def empty(a):
    pass

cv2.namedWindow("Trackbars")
cv2.createTrackbar("HUE Min", "Trackbars", 0, 179, empty)
cv2.createTrackbar("SAT Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("VAL Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("HUE Max", "Trackbars", 179, 179, empty)
cv2.createTrackbar("SAT Max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("VAL Max", "Trackbars", 255, 255, empty)

while True:
    _, img = cap.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE Min", "Trackbars")
    h_max = cv2.getTrackbarPos("HUE Max", "Trackbars")
    s_min = cv2.getTrackbarPos("SAT Min", "Trackbars")
    s_max = cv2.getTrackbarPos("SAT Max", "Trackbars")
    v_min = cv2.getTrackbarPos("VAL Min", "Trackbars")
    v_max = cv2.getTrackbarPos("VAL Max", "Trackbars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask = mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])

    cv2.imshow('Horizontal Stacking', hStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(30) >= 0:
        break

cap.release()
cv2.destroyAllWindows()