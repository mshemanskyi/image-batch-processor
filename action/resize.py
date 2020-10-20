import cv2 as cv
import numpy as np

def resizeImage(img, scale):
    kernel = np.ones((2, 2), np.uint8)
    img = cv.dilate(img, kernel, iterations=1)

    width = int(img.shape[1] * scale / 100)
    height = int(img.shape[0] * scale / 100)
    dim = (width, height)
    # resize image
    resized = cv.resize(img, dim, interpolation = cv.INTER_AREA) 
    
    return resized 