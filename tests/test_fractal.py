import unittest
from sbober_fractals import Mandelbrot

class MandelbrotTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_create(self):
        resolution = (200, 200)
        fr = Mandelbrot(resolution=resolution)
        arr = fr.calculate()
        self.assertEqual(arr.shape, resolution,
                         f"Result array resolution {arr.shape}, required {resolution}")

    def test_zero(self):
        maxit = 200
        fr = Mandelbrot(x_range=(0., 1.),
                        y_range=(0., 1.),
                        maxit=maxit)
        arr = fr.calculate()
        self.assertEqual(arr[0, 0], maxit-1,
                         f"Array[0, 0] should be {maxit-1}, got {arr[0, 0]}")