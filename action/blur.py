import cv2 as cv
import numpy as np

def blurImage(img, blur):
    kernel = np.ones((2, 2), np.uint8)
    img = cv.dilate(img, kernel, iterations=1)

    blur = cv.medianBlur(img, blur)
    
    return blur 