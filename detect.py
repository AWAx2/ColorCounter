import numpy as np
import cv2

def detect_img(frame):
    # 色の指定
    ora = np.uint8([[[0, 155, 255]]])
    hsv_ora = cv2.cvtColor(ora, cv2.COLOR_BGR2HSV)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    orange = cv2.inRange(hsv, np.array([8, 135, 135]), np.array([28, 255, 255]))
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    orange_img = cv2.erode(orange, kernel)

    image, contours, hierarchy = cv2.findContours(orange_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 誤検知排除
    count_normal = len(contours)
    contours = list(filter(lambda cnt: len(cnt) > 20, contours))
    count = len(contours)

    total = "total:{}".format(count)
    return total
