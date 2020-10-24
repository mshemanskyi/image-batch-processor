import cv2 as cv
import numpy as np

def addWatermark(img, watermarkImagePath, text):
    if watermarkImagePath:
        logo_img = cv.imread(watermarkImagePath, 1)
        return watermarkImage(img, logo_img)
    elif text:
        return watermarkText(img, text)

def watermarkImage(img, watermark):

    ih,iw = img.shape[:2]
    wh,ww = watermark.shape[:2]

    ovr = np.zeros((ih,iw,3), dtype="uint8")
    ovr[ih - wh:ih, iw - ww:iw] = watermark
    result = img.copy()
    result = cv.addWeighted(ovr,0.25,result,1.0,0,result)

    return result


def watermarkText(img, text):

    overlay = img.copy()

    h,w = img.shape[:2]
    font = cv.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (w - (len(text) * 10 + 150), h - 10)
    fontScale = 1
    fontColor = (255,255,255, 0.25)
    lineType = 2

    cv.putText(img,text, bottomLeftCornerOfText, font, fontScale, fontColor, lineType)
    alpha = 0.7

    return cv.addWeighted(overlay, alpha, img, 1 - alpha, 0)


