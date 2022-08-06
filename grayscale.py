import cv2 as cv
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory) 
        
createFolder('./img')

img = cv.imread('a.jpg', cv.IMREAD_GRAYSCALE)

cv.imwrite('./img/result.jpg', img)