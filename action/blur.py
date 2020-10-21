import cv2 as cv

def blurImage(img, blur):

    blur = cv.medianBlur(img, blur)
    
    return blur 