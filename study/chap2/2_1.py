# numpy 연습
import numpy as np

a = np.array([4,5,0,1,2,3,4,6,7,8,9,10,11])
print(a)
print(type(a))
# type을 통해 a 객체는
# 'numpy.ndarray'에 속한다는 것을 알 수 있음
print(a.shape)
a.sort()
print(a)
# print(dir(a))
# dir을 통해 a객체의 멤버함수를 알 수 있음

b = np.array([-4.3,-2.3,12.9,8.99,10.1,-1.2])
b.sort()
print(b)

c = np.array(["one","two","three","four","five","six","seven"])
c.sort()
print(c)

help(a.sort)
# help를 통해 sort 함수에 대해 알 수 있음