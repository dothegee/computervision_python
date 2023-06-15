import skimage
import numpy as np
import cv2 as cv

img = skimage.data.coffee()
cv.imshow('Coffee',cv.cvtColor(img,cv.COLOR_RGB2BGR))
cv.imshow(img)

slic1 = skimage.segmentation.slic(img,compactness = 20, n_segments=600)
sp_img1 = skimage.segmentation.ark_boundaries(img,slic1)
sp_img1 = np.uint8(sp_img1*255.0)

slic2 = skimage.segmentation.slic(img, compactness = 40, n_segments = 600)
sp_img2 = skimage.segmentation.ark_boundaries(img,slic2)
sp_img2 = np.uint8(sp_img2*255.0)

cv.imshow(cv.cvtColor(sp_img1,cv.COLOR_RGB2BGR))
cv.imshow(cv.cvtColor(sp_img2,cv.COLOR_RGB2BGR))

cv.waitKey()
cv.destroyAllWindows()