import unittest
from action.watermark import watermarkImage, watermarkText
import cv2 as cv
import numpy as np

class WatermarkTest((unittest.TestCase)):

    @classmethod
    def setUpClass(self):
        self.testImage = cv.imread('examples/img1.jpg')
        self.watermarkLogo = cv.imread('examples/wm-logo.png')

    def setUp(self):
        pass

    def test_watermak__image_action(self):
        wmi = watermarkImage(self.testImage, self.watermarkLogo)

        self.assertTrue(np.any(self.testImage != wmi))

    def test_watarmark_text_action(self):
        wmi = watermarkText(self.testImage, 'watermarkLogo')

        self.assertTrue(np.any(self.testImage != wmi))
