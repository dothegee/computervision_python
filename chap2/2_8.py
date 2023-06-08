import cv2 as cv
import sys

img = cv.imread('soccer.jpg')

print(type(img))

if img is None:
    sys.exit('파일 없음')

def draw(event, x, y, flags, param):
    global ix, iy
    if event == cv.EVENT_LBUTTONDOWN:
        ix,iy=x,y
    elif event == cv.EVENT_LBUTTONUP:
        cv.rectangle(img,(ix,iy),(x,y),(0,255,255),2)
    cv.imshow('hi',img)
    
cv.namedWindow('hi')
cv.imshow("hi",img)

cv.setMouseCallback('hi',draw)
# hi 윈도우에 draw콜백 함수 지정

while(True):
    if cv.waitKey(1)==ord('q'):
    
        cv.destroyAllWindows()

        break

