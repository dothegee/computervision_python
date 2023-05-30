import cv2 as cv
import sys

img = cv.imread("soccer.jpg")

type(img)
print(img.shape)
#(168, 299, 3)
if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

cv.imshow("Image Display", img) #윈도우 창에 띄우기
# imshow(winname, mat)
# help(cv.imshow)
cv.waitKey()
cv.destroyAllWindows()