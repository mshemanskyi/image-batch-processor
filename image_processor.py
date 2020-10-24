import cv2 as cv
import os
from datetime import datetime
from action.threshold import thresholdImage
from action.blur import blurImage
from action.resize import resizeImage
from action.rotate import rotateImage
from action.mirror import mirrorImage
from action.watermark import addWatermark

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
        scale = int(params['scale'])
        degree = int(params['degree'])
        watermarkImage = params['watermarkImage']
        watermarkText = params['watermarkText']
        action = params['action']

        saveOriginal = False

        if action == "threshold":
            processedImage = thresholdImage(img, blur, threshold, threshAdaptiveMethod, threshType, ThreshConstant)
        elif action == "blur":
            processedImage = blurImage(img, blur)
        elif action == "resize":
            processedImage = resizeImage(img, scale)
        elif action == "rotate":
            processedImage = rotateImage(img, degree)
        elif action == "mirror":
            processedImage = mirrorImage(img)
        elif action == "watermark":
            processedImage = addWatermark(img, watermarkImage, watermarkText)
        else:
            processedImage = img
        ##### func end


        filename, ext = os.path.splitext(imagePath)
        time = datetime.now().strftime("%m_%d_%YT%H-%M-%S")
        date = datetime.now().strftime("%m_%d_%Y")

        # Check if it Windows OS and build specific path
        if os.name == 'nt':
            name = filename[filename.rfind("\\") +1:] + '.' + extension
            print('Windows: output file name: ' + name)
        else:
            name = filename[filename.rfind("/") +1:] + '.' + extension

        outputFileName =  os.path.join(os.getcwd(), os.path.join('output', name))
        cv.imwrite(outputFileName, processedImage)

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
