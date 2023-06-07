import cv2 as cv
import sys

img = cv.imread('soccer.jpg')

print(type(img))

if img is None:
    sys.exit('파일 없음')

def draw(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:

        cv.rectangle(img,(x,y),(x+100,y+30),(0,0,255),2)
        # (이미지파일, 좌표1, 좌표2, 색상, 두께)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img,(x,y),(x+50,y+30),(0,255,255),2)
    cv.imshow('hi',img)
    
cv.namedWindow('hi')
cv.imshow("hi",img)

cv.setMouseCallback('hi',draw)
# hi 윈도우에 draw콜백 함수 지정

while(True):
    if cv.waitKey(1)==ord('q'):
    
        cv.destroyAllWindows()

        break

    