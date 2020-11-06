import unittest
from action.threshold import thresholdImage
import cv2 as cv

class ThresholdTest((unittest.TestCase)):

    @classmethod
    def setUpClass(self):
        self.testImage = cv.imread('examples/img1.jpg')

    def setUp(self):
        pass

    def test_threshold_action(self):
        thresh = thresholdImage(self.testImage, 5, 11, 'ADAPTIVE_THRESH_GAUSSIAN_C', 'THRESH_BINARY', 2)

        self.assertTrue(len(thresh.shape) < 3)
