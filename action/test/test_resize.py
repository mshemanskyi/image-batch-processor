import unittest
from action.resize import resizeImage
import cv2 as cv

class ResizeTest((unittest.TestCase)):

    @classmethod
    def setUpClass(self):
        self.testImage = cv.imread('examples/img1.jpg')

    def setUp(self):
        pass

    def test_resize_action(self):
        resized = resizeImage(self.testImage, 50)

        h = self.testImage.shape[0]
        w = self.testImage.shape[1]
        rh = resized.shape[0]
        rw = resized.shape[1]

        self.assertTrue(h > rh)
        self.assertTrue(w > rw)
