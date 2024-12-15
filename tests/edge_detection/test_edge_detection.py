import unittest
import cv2
import numpy as np
from src.edge_detection.EdgeDetector import EdgeDetection


class TestEdgeDetection(unittest.TestCase):
    def setUp(self):
        self.edge_detection = EdgeDetection(method='canny')
        self.test_image = np.zeros((100, 100), dtype=np.uint8)
        cv2.rectangle(self.test_image, (25, 25), (75, 75), 255, -1)

    def test_edge_detection(self):
        edges, bounding_boxes, *rest = self.edge_detection.detect_edges(self.test_image)
        self.assertIsNotNone(edges, "Edges should not be None.")
        self.assertGreater(len(bounding_boxes), 0, "There should be at least one bounding box.")

    def test_set_method(self):
        self.edge_detection.set_method('sobel')
        self.assertEqual(self.edge_detection.detect_edges, 'sobel', "Edge detection method should be 'sobel'.")

if __name__ == '__main__':
    unittest.main()