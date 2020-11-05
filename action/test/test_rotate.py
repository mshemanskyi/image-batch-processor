import unittest
from action.rotate import rotateImage
import cv2 as cv
import numpy as np

class RotateTest((unittest.TestCase)):

    @classmethod
    def setUpClass(self):
        self.testImage = cv.imread('examples/img1.jpg')

    def setUp(self):
        pass

    def test_rotate_action(self):
        rotated = rotateImage(self.testImage, 50)

        self.assertTrue(np.any(self.testImage != rotated))
