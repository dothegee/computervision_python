# 카메라 연결 하지 않은 상태

import cv2 as cv
import sys

# 카메라 연결 시도
cap = cv.VideoCapture(0, cv.CAP_DSHOW)

if not cap.isOpened():
    sys.exit("카메라 연결 실패")

while True:
    ret, frame = cap.read()
    # 비디오 구성하는 프레임 획득

    if not ret:
        print("프레임 획득에 실패하여 루프를 나갑니다")
        break
    cv.imshow("Video display", frame)

    key=cv.waitKey(1)
    if key == ord('q'):
        break

cap.relesae()
cv.destroyAllWindows()
