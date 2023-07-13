#R 채널 히스토그램 구하기

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('soccer.jpg')
h = cv.calcHist([img],[2],None,[256],[0,256])
# calcHist([영상],[영상의 채널 번호],히스토그램을 구할 영역을 지정하는 mask,[히스토그램의 칸수],명함단계)
plt.plot(h, color = 'r',linewidth = 1)
plt.show()