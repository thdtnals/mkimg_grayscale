import cv2 as cv
import os
import folder as f

f.createFolder('./img')

img = cv.imread('a.jpg', cv.IMREAD_GRAYSCALE)
cv.imwrite('./img/result.jpg', img)