import cv2 as cv

def addWatermark(img, watermarkImagePath, text):
    if watermarkImagePath:
        logo_img = cv.imread(watermarkImagePath, 0)
        return watermarkImage(img, logo_img)
    elif text:
        return watermarkText(img, text)

def watermarkImage(img, watermark):
    print("123")
    return img


def watermarkText(img, text):
    print(text)
    return img


