import cv2 as cv
import numpy as np
from pathlib import Path
from datetime import datetime
import os
import sys
import csv
 
class ImageProcessor():

    def threshold(self, imagePath, params):
        if os.name == 'nt':
            imagePath = imagePath.replace('/','\\')

        img = cv.imread(imagePath,1)
        img_orig = cv.imread(imagePath,1)

        contourSize = -1
        blur = int(params['blur'])
        threshold = int(params['threshold'])
        threshAdaptiveMethod = params['threshAdaptiveMethod']
        threshType = params['threshType']
        ThreshConstant = int(params['thresholdConstant'])

        saveOriginal = True

        kernel = np.ones((2,2), np.uint8)
        img = cv.dilate(img, kernel, iterations=1)

        contourSize = -1

        # (RGB)
        thresholdImg = thresholdImage(img, blur, threshold, threshAdaptiveMethod, threshType, ThreshConstant)


        ##### func end








        filename, ext = os.path.splitext(imagePath)
        time = datetime.now().strftime("%m_%d_%YT%H-%M-%S")
        date = datetime.now().strftime("%m_%d_%Y")

        # Check if it Windows OS and build specific path
        if os.name == 'nt':
            name = filename[filename.rfind("\\") +1:] + '_' + time + '.png'
            thresName = filename[filename.rfind("\\") +1:] + '_THRESH_' + time + '.png'
            print('Windows: output file name: ' + name)
        else:
            name = filename[filename.rfind("/") +1:] + '_' + time + '.png'
            thresName = filename[filename.rfind("/") +1:] + '_THRESH_' + time + '.png'

        outputFileName =  os.path.join(os.getcwd(), os.path.join('output', name))
        outputThreshFileName =  os.path.join(os.getcwd(), os.path.join('output', thresName))
        cv.imwrite(outputFileName, img)


        print("file saved! path: " + outputFileName)
        cv.imwrite(outputThreshFileName, thresholdImg)

        # Check if it Windows OS and build specific path
        if os.name == 'nt':
            originalName = filename[filename.rfind("\\") +1:] + ext
            print('Windows: original file name: ' + originalName)
        else:
            originalName = filename[filename.rfind("/") +1:] + ext

        originalPath = os.path.join(os.getcwd(), os.path.join("original", originalName))
        if not os.path.exists(originalPath) and saveOriginal:
            print('RENAME: ' + imagePath + ' TO ' + originalPath)
            #os.rename(imagePath, os.path.join("original", originalName))
            os.rename(imagePath, originalPath)
        else:
            os.remove(imagePath)

def thresholdImage(img, blur, threshold, threshAdaptiveMethod, threshType, const):
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