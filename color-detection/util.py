import cv2 as cv, numpy as np


def get_limits(color):
    c = np.uint8([[color]])  # BGR value to convert to HSV
    hsv_c = cv.cvtColor(c, cv.COLOR_BGR2HSV)[0][0]

    hue = int(hsv_c[0])
    lower_hue = max(hue - 10, 0)
    upper_hue = min(hue + 10, 179)

    lower_limit = np.array([lower_hue, 100, 100], dtype=np.uint8)
    upper_limit = np.array([upper_hue, 255, 255], dtype=np.uint8)

    return lower_limit, upper_limit

