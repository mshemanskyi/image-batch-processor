import unittest
from action.mirror import mirrorImage
import cv2 as cv
import numpy as np

class TestMirror(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.testImage = cv.imread('examples/img1.jpg')

    def setUp(self):
        pass

    def test_mirror_action(self):

        original = self.testImage
        mirror = mirrorImage(self.testImage)

        self.assertTrue(np.any(original != mirror))


if __name__ == '__main__':
    unittest.main()