import cv2 as cv
import numpy as np

def thresholdImage(img, blur, threshold, threshAdaptiveMethod, threshType, const):
    kernel = np.ones((2, 2), np.uint8)
    img = cv.dilate(img, kernel, iterations=1)

    img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.medianBlur(img_grey, blur)
    thresholdImg = cv.adaptiveThreshold(blur, 255, getAdaptiveThresholdMethod(threshAdaptiveMethod),
                                        getThresholdType(threshType), threshold, const)
    return thresholdImg

def getAdaptiveThresholdMethod(threshAdaptiveMethod):
    if threshAdaptiveMethod == 'ADAPTIVE_THRESH_GAUSSIAN_C':
        return cv.ADAPTIVE_THRESH_GAUSSIAN_C
    elif threshAdaptiveMethod == 'ADAPTIVE_THRESH_MEAN_C':
        return cv.ADAPTIVE_THRESH_MEAN_C

def getThresholdType(threshType):
    if threshType == 'THRESH_BINARY':
        return cv.THRESH_BINARY
    elif threshType == 'THRESH_BINARY_INV':
        return cv.THRESH_BINARY_INV