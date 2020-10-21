import cv2 as cv

def rotateImage(img, degree):

    rows = img.shape[0]
    cols = img.shape[1]

    M = cv.getRotationMatrix2D((cols/2,rows/2), degree, 1)
    dst = cv.warpAffine(img,M,(cols,rows))
    
    return dst 