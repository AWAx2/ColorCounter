import sys
import cv2
from detect import detect_img

if __name__ == "__main__":
    cycle = 90  # 保存間隔を指定
    n = 1

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error：カメラが起動できませんでした")
        sys.exit()
    else:
        print("\"Q\"を押すと終了")

    while True:
        ret, frame = cap.read()
        cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)
        cv2.imshow("Camera", frame)

        k = cv2.waitKey(1) & 0xff

        if n % cycle == 0:
            total = detect_img(frame)
            print(total)
        elif k == ord("q"):
            break

        n += 1

    cap.release()
    cv2.destroyAllWindows()
