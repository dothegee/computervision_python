import cv2 as cv
img = cv.imread('apple.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

apples = cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,70,param1=150,param2=20,minRadius=5,maxRadius=120)

for i in apples[0]:
    cv.circle(img,(int(i[0]),int(i[1])),int(i[2]),(255,0,255),2)

cv.imshow('Apple',img)

cv.waitKey()
cv.destroyAllWindows()
