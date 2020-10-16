import cv2 as cv
import os
from datetime import datetime
from action.threshold import thresholdImage

class ImageProcessor():

    def do(self, imagePath, params):
        if os.name == 'nt':
            imagePath = imagePath.replace('/','\\')

        img = cv.imread(imagePath,1)

        blur = int(params['blur'])
        threshold = int(params['threshold'])
        threshAdaptiveMethod = params['threshAdaptiveMethod']
        threshType = params['threshType']
        ThreshConstant = int(params['thresholdConstant'])
        extension = params['extension']

        saveOriginal = False

        # (RGB)
        thresholdImg = thresholdImage(img, blur, threshold, threshAdaptiveMethod, threshType, ThreshConstant)


        ##### func end


        filename, ext = os.path.splitext(imagePath)
        time = datetime.now().strftime("%m_%d_%YT%H-%M-%S")
        date = datetime.now().strftime("%m_%d_%Y")

        # Check if it Windows OS and build specific path
        if os.name == 'nt':
            name = filename[filename.rfind("\\") +1:] + '_' + time + '.' + extension
            thresName = filename[filename.rfind("\\") +1:] + '_THRESH_' + time + '.' + extension
            print('Windows: output file name: ' + name)
        else:
            name = filename[filename.rfind("/") +1:] + '_' + time + '.' + extension
            thresName = filename[filename.rfind("/") +1:] + '_THRESH_' + time + '.' + extension

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
            os.rename(imagePath, originalPath)
        else:
            os.remove(imagePath)
