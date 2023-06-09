#오츄 알고리즘

import cv2 as cv
import sys

img = cv.imread('soccer.jpg')

t, bin_img = cv.threshold(img[:,:,2],0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
print(f'오츄 알고리즘이 찾은 최적 임계값 : {t}')

cv.imshow('Rchannel',img[:,:,2])
cv.imshow('R channel Bin',bin_img)

cv.waitKey()
cv.destroyAllWindows()