import unittest
from action.blur import blurImage
import cv2 as cv

class TestBlur(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.testImage = cv.imread('examples/img1.jpg')

    def setUp(self):
        pass

    def test_blur_action(self):
        blurred = blurImage(self.testImage, 5)
        self.assertIsNotNone(blurred)


if __name__ == '__main__':
    unittest.main()