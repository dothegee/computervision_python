import cv2 as cv
import sys

img = cv.imread('soccer.jpg')

print(type(img))

if img is None:
    sys.exit('파일 없음')

cv.rectangle(img,(200,70),(100,50),(0,0,255),2)
# (이미지파일, 좌표1, 좌표2, 색상, 두께)

cv.putText(img,'soccer',(100,40),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2) 

cv.imshow("hi",img)

cv.waitKey()
cv.destroyAllWindows()