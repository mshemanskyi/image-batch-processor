import cv2 as cv

def mirrorImage(img):

    mirror = cv.flip(img, 1)

    return mirror