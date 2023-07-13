# 영상을 명암 영상을 변환하고 반으로 축소하기
import cv2 as cv
import sys

img = cv.imread("soccer.jpg")

type(img)
print(img.shape)
#(168, 299, 3)
if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

#BGR 컬러 영상을 흑백으로 변환
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#반으로 축소
gray_small = cv.resize(gray,dsize=(0,0),fx=0.5,fy=0.5)
#  dsize = (0, 0) 으로 결과 이미지 크기를 설정하지 않은 경우
# fx, fy를 통해 이미지 비율을 조절 가능
# ex) dsize = (100,200) 으로 하게 되면 가로 100 세로 200 크기로 설정됨

# help(cv.resize)

# 이미지 저장
cv.imwrite('soccer_gray.jpg',gray)
cv.imwrite('soccer_gray_small.jpg',gray_small)


cv.imshow("Image Display", img) #윈도우 창에 띄우기
cv.waitKey()
cv.imshow("Image Display", gray) #윈도우 창에 띄우기
cv.waitKey()
cv.imshow("Image Display", gray_small) #윈도우 창에 띄우기

# imshow(winname, mat)
# help(cv.imshow)
cv.waitKey()
cv.destroyAllWindows()